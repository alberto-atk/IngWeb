"""locallibrary URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.views.generic import RedirectView
from django.conf import settings
from django.conf.urls.static import static
from django.urls import include
from django.urls import include, re_path
from catalog import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('catalog/', include('catalog.urls')),
    path('accounts/', include('django.contrib.auth.urls')),
    path('register/registerUser', views.registerUser, name='registerUser'),
    path('bookings/getBookings', views.getAvailableBookings, name='getAvailableBookings'),
    re_path('bookings/deleteBooking', views.deleteBooking, name='deleteBooking'),
    path('settings/changeSettings', views.changeSettings, name='changeSettings'),
    path('', RedirectView.as_view(url='catalog/')),
    re_path(r'^register/$', views.register, name='register'),
    re_path(r'^contact/$', views.contact, name='contact'),
    re_path(r'^aboutme/$', views.aboutme, name='aboutme'),
    re_path(r'^bookings/$', views.bookings, name='bookings'),
    re_path(r'^settings/$', views.settings, name='settings'),
    re_path(r'^editPublications/$', views.editPublications, name='editPublications'),
    re_path(r'^bookings/makeBooking', views.makeBooking, name='makeBooking'),
    re_path(r'^publicationDetails/(?P<pk>\d+)$',views.publicationDetails, name='publicationDetails'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)