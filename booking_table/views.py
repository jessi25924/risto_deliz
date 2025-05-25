from django.shortcuts import render, redirect
from django.contrib.auth import login
from .forms import SignUpForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LoginView
from .forms import BookingForm
from .models import Booking
from datetime import datetime
from django.db import IntegrityError

def signup(request):
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
    return render(request, 'booking_table/dashboard.html')


class CustomLoginView(LoginView):
    """Custom login view using the booking_table login template."""
    template_name = 'booking_table/login.html'


# Time slots
ALL_SLOTS = [
    "12:00", "12:30", "13:00", "13:30", "14:00", "14:30",
    "17:00", "17:30", "18:00", "18:30", "19:00", "19:30"
]

@login_required
def book_table(request):
    """
    Display and process the booking form.

    Filters the form.time.choices based on 'date' and 'table' from
    either GET (for initial slot loading) or POST (so slots persist).
    """
    # Grab date & table from GET or POST
    date_str = request.GET.get('date') or request.POST.get('date')
    table_id = request.GET.get('table') or request.POST.get('table')

    # Bind the form to POST data if present
    form = BookingForm(request.POST or None)

    # If we have both date and table, filter time choices
    if date_str and table_id:
        try:
            date = datetime.strptime(date_str, '%d-%m-%Y').date()
            # times already booked
            booked = Booking.objects.filter(
                date=date, table_id=table_id
            ).values_list('time', flat=True)
            # build remaining slots
            choices = [(t, t) for t in ALL_SLOTS if t not in booked]
            if not choices:
                choices = [('', 'No availability')]
        except Exception:
            choices = [('', 'No availability')]

        form.fields['time'].choices = choices

    # On POST, if valid, save and redirect
    if request.method == 'POST' and form.is_valid():
        booking = form.save(commit=False)
        booking.user = request.user
        booking.save()
        return redirect('dashboard')

    return render(request, 'booking_table/book.html', {
        'form': form,
        'selected_date': date_str or '',
        'selected_table': table_id or '',
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
    Mark a booking as cancelled.
    """
    booking = get_object_or_404(Booking, pk=pk, user=request.user)
    booking.status = 'Cancelled'
    booking.save()
    return redirect('dashboard')