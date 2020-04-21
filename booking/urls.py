from django.urls import path

from booking.api import views


urlpatterns = [
    path(r'', views.booking_view, name='book'),
]
