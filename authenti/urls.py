from django.urls import path

from authenti.api import views


urlpatterns = [
    path(r'signup/', views.signup_view, name='signup'),
   # path(r'signin', views.signin_view, name='signin'),
   # path(r'signout', views.signout_view, name='signout'),
   # path(r'verifyotp', views.verifyotp_view, name='verifyotp')
]
