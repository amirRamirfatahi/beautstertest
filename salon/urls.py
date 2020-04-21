from django.urls import path

from salon.api import views


urlpatterns = [
    path(r'', views.listsalon_view, name='salons'),
    path(r'<pk>', views.salon_view, name='salon')
]
