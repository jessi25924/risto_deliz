from django.shortcuts import render, redirect
from django.contrib.auth import login
from .forms import SignUpForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LoginView
from .forms import BookingForm
from .models import Booking
from datetime import datetime

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
    
    GET params:
        - date (DD-MM-YYYY)
        - table (table)
    
    After selecting a date and table, the form's time choices get overriden
    to only show free slots (or "No Availability").

    On POST, validates and saves a booking linked to request.user.
    """

    # (unbound for GET, or bound for POST)
    form = BookingForm(request.POST or None)

    # If the user has selected date & table, filter time choices
    date_str = request.GET.get('date')
    table_id = request.GET.get('table')
    if date_str and table_id:
        try:
            date = datetime.strptime(date_str, '%d-%m-%Y').date()
            # Find times already booked for that date+table
            booked = Booking.objects.filter(date=date, table_id=table_id)\
                                    .values_list('time', flat=True)
            # Build available choices
            choices = [(t, t) for t in ALL_SLOTS if t not in booked]
            if not choices:
                # No slots left
                choices = [('', 'No availability')]
        except Exception:
            # In case of parsing errors or invalid table_id
            choices = [('', 'No availability')]

        # Override only the 'time' field on the form
        form.fields['time'].choices = choices

    # Handle submission
    if request.method == 'POST':
        if form.is_valid():
            booking = form.save(commit=False)
            booking.user = request.user
            booking.save()
            return redirect('dashboard')  # make sure this name is correct!

    # Pass along selected date/table so template can keep them
    context = {
        'form': form,
        'selected_date': date_str or '',
        'selected_table': table_id or '',
    }
    return render(request, 'booking_table/book.html', context)
