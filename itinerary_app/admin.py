from django.contrib import admin
from .models import EventModel, HotelModel, RestaurantModel, TouristModel
# Register your models here.

admin.site.register(EventModel)
admin.site.register(RestaurantModel)
admin.site.register(HotelModel)
admin.site.register(TouristModel)
