from django.shortcuts import render, redirect
from django.contrib.auth import login
from .forms import SignUpForm

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
