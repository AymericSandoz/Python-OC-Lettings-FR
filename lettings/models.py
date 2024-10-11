from django.db import models
from django.core.validators import MaxValueValidator, MinLengthValidator
# Create your models here.


class Address(models.Model):
    """Model representing an address.

    Attributes:
        number (int): The street number.
        street (str): The street name.
        city (str): The city name.
        state (str): The state abbreviation.
        zip_code (int): The ZIP code.
        country_iso_code (str): The country ISO code.

    Relationships:
        None
    """
    number = models.PositiveIntegerField(validators=[MaxValueValidator(9999)])
    street = models.CharField(max_length=64)
    city = models.CharField(max_length=64)
    state = models.CharField(max_length=2, validators=[MinLengthValidator(2)])
    zip_code = models.PositiveIntegerField(
        validators=[MaxValueValidator(99999)])
    country_iso_code = models.CharField(
        max_length=3, validators=[MinLengthValidator(3)])

    class Meta:
        verbose_name = "adresse"
        verbose_name_plural = "adresses"

    def __str__(self):
        return f'{self.number} {self.street}'


class Letting(models.Model):
    """Model representing a letting.

    Attributes:
        title (str): The letting title.
        address (Address): The address of the letting.

    Relationships:
        address (Address): The address of the letting.
    """
    title = models.CharField(max_length=256)
    address = models.OneToOneField(Address, on_delete=models.CASCADE)

    def __str__(self):
        return self.title
