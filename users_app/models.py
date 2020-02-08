from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    LOCATION_CHOICE = (
        ('Kathmandu', 'Kathmandu'),
        ('Pokhara', 'Pokhara'),
        ('Chitwan', 'Chitwan'),
    )
    THEME_CHOICE = (
        ('adventure', 'adventure'),
        ('nature', 'nature'),
        ('culture', 'culture'),
        ('food', 'food'),
        ('entertainment', 'entertainment'),
        ('leisure', 'leisure')

    )
    location = models.CharField(max_length=255, choices=LOCATION_CHOICE)
    theme = models.CharField(max_length=255, choices=THEME_CHOICE)

    def __str__(self):
        return f'{self.user.username} Profile'
