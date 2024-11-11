from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Profile(models.Model):
    """Model representing a user profile.

    Attributes:
        user (User): One-to-one relationship with the User model.
        favorite_city (str): The user's favorite city.

    Relationships:
        user (User): One-to-one relationship with the User model.
    """

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    favorite_city = models.CharField(max_length=64, blank=True)

    # class Meta:
    #     db_table = 'oc_lettings_site_profile'

    def __str__(self):
        return self.user.username
