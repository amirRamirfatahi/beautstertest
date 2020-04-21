from rest_framework import status
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from django.contrib.auth import get_user_model
from django.views.generic import TemplateView
from django.shortcuts import redirect, reverse

from utils.views import BaseAPIView
from authenti.api import serializers
from authenti.tasks import send_otp_mail


class VerifyotpView(BaseAPIView, TemplateView):
    serializer_class = serializers.VerifyotpSerializer
    permission_classes = [AllowAny]
    lookup_field = 'username'
    queryset=get_user_model().objects.all()
    template_name = 'verifyotp.html'

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data,
                                         instance=self.get_object())
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(data=serializer.data, status=status.HTTP_202_ACCEPTED)


verifyotp_view = VerifyotpView.as_view()
