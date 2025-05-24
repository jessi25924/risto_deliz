from django.shortcuts import render, redirect
from django.contrib.auth import login
from .forms import SignUpForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LoginView
from .forms import BookingForm

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


@login_required
def book_table(request):
    """
    Display and process the booking form.
    fields: table, dtae, time, guest_count, email, phone, suggestion.

    On valid submission, creates a Booking linked to the logged-in user
    and then redirects to the dshboard.
    """
    if request.method == 'POST':
        form = BookingForm(request.POST)
        if form.is_valid():
            booking = form.save(commit=False)
            booking.user = request.user
            booking.save()
            return redirect('dahsboard')
    else:
        form = BookingForm()
    return render(request, 'booking_table/book.html', {'form': form})