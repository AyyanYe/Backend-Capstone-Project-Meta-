from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator

# Create your models here.
class Booking(models.Model):
    ID = models.IntegerField(
        primary_key=True,
        validators=[MaxValueValidator(99999999999), MinValueValidator(1)],
        null=False,
        blank=False
    )
    Name = models.CharField(max_length=255)
    No_of_guests = models.IntegerField(
        validators=[MaxValueValidator(999999), MinValueValidator(1)]
    )
    BookingDate = models.DateTimeField()

class Menu(models.Model):
    ID = models.IntegerField(
        primary_key=True,
        validators=[MaxValueValidator(99999), MinValueValidator(1)],
        null=False,
        blank=False
    )
    Title = models.CharField(max_length=255)
    Price = models.DecimalField(max_digits=10, decimal_places=2)
    Inventory = models.IntegerField(
        validators=[MaxValueValidator(99999), MinValueValidator(0)]
    )