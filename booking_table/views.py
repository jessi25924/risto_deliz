from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login
from .forms import SignUpForm, BookingForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LoginView
from .models import Booking, MenuItem
from collections import defaultdict

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
    template_name = 'booking_table/login.html'


@login_required
def book_table(request):
    """
    Display and process the booking form with HTML5 date & time pickers.
    """
    # Bind the form to POST data (or unbound if GET)
    form = BookingForm(request.POST or None)

    # On POST: validate, save, and redirect
    if request.method == 'POST' and form.is_valid():
        booking = form.save(commit=False)
        booking.user = request.user
        booking.save()
        return redirect('dashboard')

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
    Mark a booking as cancelled.
    """
    booking = get_object_or_404(Booking, pk=pk, user=request.user)
    booking.status = 'Cancelled'
    booking.save()
    return redirect('dashboard')


def menu_view(request):
    """
    Dsiplay the menu items grouped by category.
    """
    items = MenuItem.objects.all().order_by('category', 'name')
    categories = defaultdict(list)
    for item in items:
        categories[item.category].append(item)
    return render(request, 'booking_table/menu.html', {'categories': categories})