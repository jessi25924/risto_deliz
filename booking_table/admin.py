from django.contrib import admin, messages
from .models import Table, Booking
from .models import MenuItem
from django.core.exceptions import ValidationError
from django.db.models import Sum

# Register your models here.
@admin.register(Booking)
class BookingAdmin(admin.ModelAdmin):
    """
    Admin interface for managing bookings.
    """
    list_display = (
        'user', 'date', 'time', 'guest_count', 'email', 'phone', 'status'
    )
    list_filter = ('date', 'status')
    ordering = ('date', 'time')

    def save_model(self, request, obj, form, change):
        # Total guest count at this date/time excluding the current booking (for edit)
        total_guests = Booking.objects.filter(
            date=obj.date,
            time=obj.time
        ).exclude(pk=obj.pk).aggregate(Sum('guest_count'))['guest_count__sum'] or 0

        # Check capacity limit
        if total_guests + obj.guest_count > 20:
            self.message_user(
                request,
                "Cannot exceed 20 guests at this time slot.",
                level=messages.ERROR
            )
            return  # Prevent saving
       
        # Auto-assign a suitable table if not manually selected
        if not obj.table:
            suitable_table = Table.objects.filter(
                seating_capacity__gte=obj.guest_count
            ).order_by('seating_capacity').first()
            if suitable_table:
                obj.table = suitable_table
            else:
                self.message_user(
                    request,
                    "No available table for this guest size.",
                    level=messages.ERROR
                )
                return  # Prevent saving

        super().save_model(request, obj, form, change)


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