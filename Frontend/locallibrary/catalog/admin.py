from django.contrib import admin

# Register your models here.
from .models import Client, Booking

admin.site.register(Client)
admin.site.register(Booking)
