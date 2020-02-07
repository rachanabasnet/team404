from django.db import models

# Create your models here.


class EventModel(models.Model):
    e_name = models.CharField(max_length=255)
    e_location = models.CharField(max_length=255)
    e_image = models.ImageField(upload_to='EventImg', blank=True, null=True)
    e_description = models.TextField(max_length=1500)
    e_duration = models.CharField(max_length=255)
    THEME_CHOICE = (
        ('adventure', 'adventure'),
        ('nature', 'nature'),
        ('culture', 'culture'),
        ('food', 'food'),
        ('entertainment', 'entertainment'),
        ('leisure', 'leisure')

    )
    e_theme = models.CharField(max_length=6, choices=THEME_CHOICE)

    def __str__(self):
        return self.e_name


class TouristModel(models.Model):
    t_name = models.CharField(max_length=255)
    t_location = models.CharField(max_length=255)

    def __str__(self):
        return self.t_name


class RestaurantModel(models.Model):
    r_name = models.CharField(max_length=255)
    r_location = models.CharField(max_length=255)
    r_description = models.TextField(max_length=1500)

    def __str__(self):
        return self.r_name


class HotelModel(models.Model):
    h_name = models.CharField(max_length=255)
    h_location = models.CharField(max_length=255)
    h_description = models.TextField(max_length=1500)

    def __str__(self):
        return self.h_name
