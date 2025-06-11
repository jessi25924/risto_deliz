from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Booking, Table
from django.core.exceptions import ValidationError


class SignUpForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        placeholders = {
            'username': 'username',
            'first_name': 'first name',
            'last_name': 'last name',
            'email': 'email',
            'password1': 'password',
            'password2': 'confirm password',
        }
        for field_name, field in self.fields.items():
            field.widget.attrs['placeholder'] = placeholders.get(field_name, '')


class BookingForm(forms.ModelForm):
    """
    Interface for adding or modifying a booking with fields for contact information and suggestion or request.
    Custom widgets added to enable date and time pickers.
    """
    class Meta:
        model = Booking
        fields = (
            'date', 'time', 'guest_count', 'email', 'phone', 'suggestion'
        )
        widgets = {
            'date': forms.DateInput(attrs={'type': 'date'}),
            'time': forms.TimeInput(attrs={'type': 'time'}),
        }
            
    # Idea suggested by Lewis (Cohort facilitator):
    # Prefill email field with logged-in user's email
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if 'email' in self.fields:
            self.fields['email'].widget.attrs['readonly'] = True

    def clean_guest_count(self):
        count = self.cleaned_data['guest_count']
        if count > 20:
            raise ValidationError(
                "Sorry, we cannot accept your booking. Capacity exceeded."
            )
        return count
