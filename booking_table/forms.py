from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Booking
from .models import Table

class SignUpForm(UserCreationForm):
    first_name = forms.CharField(max_length=50, required=True, help_text='Your given name')
    last_name  = forms.CharField(max_length=50, required=True, help_text='Your family name')
    email      = forms.EmailField(max_length=254, required=True, help_text='Enter a valid email address')

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2')


class BookingForm(forms.ModelForm):
    """
    Interface for adding or modifying a booking with fields for contact information and suggestion or request.
    Custom widgets added to enable date and time pickers.
    """
    class Meta:
        model = Booking
        fields = (
            'table', 'date', 'time', 'guest_count', 'email', 'phone', 'suggestion'
        )
        widgets = {
            'date': forms.DateInput(attrs={'type': 'date'}),
            'time': forms.TimeInput(attrs={'type': 'time'}),
        }