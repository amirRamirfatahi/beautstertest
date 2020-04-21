from django.urls import path

from salon.api import views


urlpatterns = [
    path(r'', views.listsalon_view, name='salons'),
]
