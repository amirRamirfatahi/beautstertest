from rest_framework.generics import CreateAPIView
from rest_framework.permissions import AllowAny
from django.contrib.auth import get_user_model
from django.views.generic import TemplateView

from authenti.api import serializers


class SignupView(CreateAPIView, TemplateView):
    serializer_class = serializers.SignupSerializer
    permission_classes = [AllowAny]
    template_name = 'signup.html'


signup_view = SignupView.as_view()
