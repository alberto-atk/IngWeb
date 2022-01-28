from django.contrib import admin

# Register your models here.
from .models import Client, Booking, Worker

admin.site.register(Client)
admin.site.register(Booking)
admin.site.register(Worker)
