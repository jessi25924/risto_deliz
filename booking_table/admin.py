from django.contrib import admin
from .models import Table, Booking

# Register your models here.
@admin.register(Booking)
class BookingAdmin(admin.ModelAdmin):
    """
    Admin view for the Booking model.
    """
    list_display = (
        'user', 'table', 'date', 'time', 'guest_count', 'email', 'phone', 'status'
    )
    list_filter = ('date', 'status')
    ordering = ('date', 'time')