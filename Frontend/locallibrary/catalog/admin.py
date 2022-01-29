from django.contrib import admin

# Register your models here.
from .models import Client, Booking, Worker, Publication

admin.site.register(Client)
admin.site.register(Booking)
admin.site.register(Worker)
admin.site.register(Publication)

