from rest_framework import status
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from django.contrib.auth import get_user_model
from django.views.generic import TemplateView
from django.shortcuts import redirect, reverse

from utils.views import BaseAPIView
from authenti.api import serializers
from authenti.tasks import send_otp_mail


class SigninView(BaseAPIView, TemplateView):
    serializer_class = serializers.SigninSerializer
    permission_classes = [AllowAny]
    lookup_field = 'username'
    queryset=get_user_model().objects.all()
    template_name = 'signin.html'

    def post(self, request, *args, **kwargs):
        redirect_url = request.data.pop('redirect_url', None)
        serializer = self.get_serializer(data=request.data,
                                         instance=self.get_object())
        serializer.is_valid(raise_exception=True)
        serializer.save()
        send_otp_mail(serializer.instance.id)
        # send_otp_mail will be used with .delay() in a real backend
        # we're avoiding that to save the hassle of running celery to
        # see a working version of our project.
        redirect_path = reverse('auth:verifyotp')
        if redirect_url:
            redirect_path += '?redirect_url={param}'.format(param=redirect_url)
        return redirect(redirect_path)
        # this should definitely return a json response indicating that
        # the otp has been sent and the redirect should preferrably be handled
        # by the client. since we want to deal with js as least as possible,
        # we handle it by the view.


signin_view = SigninView.as_view()
