from rest_framework.generics import CreateAPIView
from rest_framework.permissions import AllowAny
from django.contrib.auth import get_user_model

from authenti.api import serializers


class SignupView(CreateAPIView):
    serializer_class = serializers.SignupSerializer
    permission_classes = [AllowAny]


signup_view = SignupView.as_view()
