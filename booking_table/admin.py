from django.contrib import admin
from .models import Table, Booking
from .models import MenuItem

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


@admin.register(Table)
class TableAdmin(admin.ModelAdmin):
    """
    Admin interface for managing restaurant tables.
    """
    list_display = ('table_number', 'seating_capacity')
    ordering = ('table_number',)


class MenuItemAdmin(admin.ModelAdmin):
    """
    Admin configuration for the MenuItem model. 
    """
    list_display = ('name', 'category', 'price')

admin.site.register(MenuItem, MenuItemAdmin)