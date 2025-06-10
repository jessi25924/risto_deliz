from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login
from .forms import SignUpForm, BookingForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LoginView
from .models import Booking, MenuItem, Table
from django.core.mail import send_mail
from django.urls import reverse
from django.conf import settings
from django.contrib import messages
from django.db.models import Sum
from datetime import datetime, date


def home(request):
    """
    Landing page with site introduction
    """
    return render(request, 'home.html')

def signup(request):
    """
    Handle user signup process.
    If the request method is POST, validate and process the submitted SignUpForm.
    If valid, create a new user, log them in, and redirect to the dashboard.
    if the request mehtod is GET, display a blank signup form.
    """
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)  # logs the user in immediately
            return redirect('dashboard')
    else:
        form = SignUpForm()
    return render(request, 'booking_table/signup.html', {'form': form})


@login_required
def dashboard(request):
    """
    Display the logged-in users booking on the dashboard, ordereed by date and time.
    """
    bookings = Booking.objects.filter(user=request.user).order_by('date', 'time')
    return render(request, 'booking_table/dashboard.html', {'bookings': bookings})


class CustomLoginView(LoginView):
    """Custom login view using the booking_table login template."""
    template_name = 'registration/login.html'


MAX_CAPACITY = 20

@login_required
def book_table(request):
    """
    Display/process the booking form with HTML5 date & time pickers.
    Enforce a 20-guest per slot capacity. On success, send confirmation email
    and render a success template.
    """
    # Prefill email if user is logged in
    initial_data = {'email': request.user.email} if request.user.is_authenticated else {}

    form = BookingForm(request.POST or None, initial=initial_data)

    if request.method == 'POST' and form.is_valid():
        booking = form.save(commit=False)
        booking.user = request.user

        # Check for past date/time
        booking_datetime = datetime.combine(booking.date, booking.time)
        if booking_datetime < datetime.now():
            form.add_error(None, "You cannot book a table in the past.")
        else:
            # 1. Sum existing guests at this date+time
            agg = Booking.objects.filter(
                date=booking.date,
                time=booking.time
            ).aggregate(total=Sum('guest_count'))
            current_total = agg['total'] or 0

            # 2. Capacity check
            if current_total + booking.guest_count > MAX_CAPACITY:
                form.add_error(
                    None,
                    f"Sorry, we’ve reached our {MAX_CAPACITY}-guest capacity for that slot. "
                    "Please choose another time or reduce your party size."
                )
            else:
                # 2. Automated table assignment
                booked_ids = Booking.objects.filter(
                    date=booking.date,
                    time=booking.time
                ).values_list('table_id', flat=True)

                available = Table.objects.exclude(id__in=booked_ids)\
                                         .filter(seating_capacity__gte=booking.guest_count)

                if not available.exists():
                    form.add_error(None,
                        "Sorry, no table is available for that size party at that time."
                    )
                else:
                    booking.table = available.first()
                    booking.save()

                    # 3. Confirmation email + success page
                    send_mail(
                        subject='Booking Request Confirmation',
                        message=(
                            f"Hi {booking.user.username},\n\n"
                            f"Thank you for reserving on {booking.date} at {booking.time} "
                            f"for {booking.guest_count} guest(s).\n\n"
                            "This isn’t final yet—our staff will confirm shortly."
                        ),
                        from_email=settings.DEFAULT_FROM_EMAIL,
                        recipient_list=[booking.email],
                        fail_silently=False,
                    )
                    return render(request, 'booking_table/booking_success.html')

    return render(request, 'booking_table/book.html', {'form': form})


@login_required
def edit_booking(request, pk):
    """
    Let user edit their booking while enforcing 20 guests limit per slot.
    """
    booking = get_object_or_404(Booking, pk=pk, user=request.user)
    form = BookingForm(request.POST or None, instance=booking)

    if request.method == 'POST' and form.is_valid():
        updated = form.save(commit=False)

        # Prevent setting booking in the past
        updated_datetime = datetime.combine(updated.date, updated.time)
        if updated_datetime < datetime.now():
            form.add_error(None, "You cannot set a booking in the past.")
        else:
            # total guest at this slot, excluding this booking
            total = Booking.objects.filter(
                date=updated.date, time=updated.time
            ).exclude(pk=booking.pk).aggregate(Sum('guest_count'))['guest_count__sum'] or 0

            if total + updated.guest_count > 20:
                form.add_error(None, "Sorry, that slot is fully booked.")
            else:
                updated.save()
                return redirect('dashboard')

    return render(request, 'booking_table/edit_booking.html', {
        'form': form,
        'booking': booking,
    })


@login_required
def cancel_booking(request, pk):
    """
    COnfirm and process booking cancellation.
    GET: show a confirmation page.
    POST: mark as cancelled and show a success page.
    """
    booking = get_object_or_404(Booking, pk=pk, user=request.user)
    
    if request.method == 'POST':
        # user confirmed cancellation
        booking.status = 'Cancelled'
        booking.save()
        return render(request, 'booking_table/cancel_success.html', {
            'booking': booking
        })
    
    # GET: ask for confirmaiton
    return render(request, 'booking_table/confirm_cancel.html', {
        'booking': booking
    })


def menu(request):
    """
    Dsiplay the menu items grouped by category.
    """
    items = MenuItem.objects.all()
    grouped_items = {}

    for item in items:
        category = item.category
        if category not in grouped_items:
            grouped_items[category] = []
        grouped_items[category].append(item)

    return render(request, 'booking_table/menu.html', {'grouped_items': grouped_items})
