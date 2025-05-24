from django.db import models
from django.conf import settings

# Create your models here.
class Table(models.Model):
    """
    Implement the restaurant table structure.

    Attributes:
    table_number: An identifier assigned to each table.
    seating_capacity: Maximum occupancy
    """
    table_number = models.PositiveIntegerField(unique=True)
    seating_capacity = models.PositiveIntegerField()

    def __str__(self):
        """
        provides a user-friendly display, e.g. "Table 1 (Seats: 2)".
        """
        return f"Table {self.table_number} (Seat: {self.seating_capacity})"


class Booking(models.Model):
    """
    Holds information about a table reservation made by a user for specific table, date, and time.

    Attributes:
    user : User who made the booking.
    table: The Table being reserved.
    date : Reservation date.
    time : Reservation time.
    guest_count: Number of guests.
    email: Contact email for this booking.
    phone: Contact phone number.
    suggestion: Optional guest suggestions or request.
    status: Current status e.g. "Pending".
    """
    STATUS_CHOICES = [
        ('Pending', 'Pending'),
        ('Cancelled', 'Cancelled'),
        ('Confirmed', 'Confirmed'),
        ('Completed', 'Completed'),
        ('No Show', 'No Show'),
    ]

    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
    )
    table = models.ForeignKey(
        'Table',
        on_delete=models.CASCADE,
    )
    date = models.DateField()
    time = models.TimeField()
    guest_count = models.PositiveIntegerField()
    email = models.EmailField(max_length=250)
    phone = models.CharField(max_length=20)
    suggestion = models.TextField(blank=True)
    status = models.CharField(
        max_length=10,
        choices=STATUS_CHOICES,
        default='Pending'
    )

    class Meta:
        ordering = ['date', 'time']
        
    
    def __str__(self):
        """
        e.g. "User - Table 1 on 24-05-2025 at 13:00 (4 guests)"
        """
        return (
            f"{self.user.username} - {self.table} on {self.date} at {self.time}"
            f"({self.guest_count} guests)"
        )