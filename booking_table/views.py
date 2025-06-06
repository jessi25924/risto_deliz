from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login
from .forms import SignUpForm, BookingForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LoginView
from .models import Booking, MenuItem
from django.core.mail import send_mail
from django.urls import reverse
from django.conf import settings
from django.contrib import messages


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


@login_required
def book_table(request):
    """
    Display and process the booking form with HTML5 date & time pickers.
    On successful booking, send confirmatoin email with booking details.
    Render a success template with link to dashboard.
    """

    # set initial if user is authenticated / Idea suggested by Lewis (Cohort facilitator): Prefill email field with logged-in user's email
    initial_data = {}
    if request.user.is_authenticated:
        initial_data['email'] = request.user.email

    # Create form with initial data
    form = BookingForm(request.POST or None, initial=initial_data)

    # On POST: validate, save, and redirect
    if request.method == 'POST' and form.is_valid():
        booking = form.save(commit=False)
        booking.user = request.user
        booking.save()

        # Compose confirmation email
        message = (
            f"Hi {booking.user.username},\n\n"
            f"Thank you for reserving a table on {booking.date} at {booking.time}.\n"
            f"For {booking.guest_count} guest.\n\n"
            f"This is not a confirmation yet, a member of staff will contact you shortly to confirm your table."
        )
        #Idea suggested by Lewis (Cohort facilitator)
        send_mail(
            subject='Booking Request Confirmation',
            message=message,
            from_email=settings.DEFAULT_FROM_EMAIL,
            recipient_list=[booking.email], 
            fail_silently=False,
        )
        #render success page instead of redirect
        return render(request, 'booking_table/booking_success.html') 

    # Render the form (empty or with errors)
    return render(request, 'booking_table/book.html', {
        'form': form,
    })


@login_required
def edit_booking(request, pk):
    """
    Let user edit their booking.
    If a unique_together violation occurs, show an error message.
    """
    booking = get_object_or_404(Booking, pk=pk, user=request.user)
    form = BookingForm(request.POST or None, instance=booking)
    error = None

    if request.method == 'POST':
        try:
            if form.is_valid():
                form.save()
                return redirect('dashboard')
        except IntegrityError:
            error = "Table is already booked at the selected date and time"
    
    return render(request, 'booking_table/edit_booking.html', {
        'form': form,
        'booking': booking,
        'error': error,
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
