from django.db import models
from django import settings

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