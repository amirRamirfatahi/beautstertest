import string
import random
import binascii
import os

from django.contrib.auth.models import AbstractBaseUser, UserManager, \
    PermissionsMixin
from django.db import models
from django.core.cache import cache

from authenti.constants import OTP_LENGTH


class CustomUserManager(UserManager):
    pass


class User(AbstractBaseUser, PermissionsMixin):
    username = models.CharField(max_length=150, unique=True)
    email = models.EmailField(unique=True)
    otp = models.CharField(max_length=OTP_LENGTH, blank=True, null=True)
    token = models.CharField(max_length=40, unique=True, blank=True, null=True)

    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)

    objects = CustomUserManager()

    USERNAME_FIELD = 'username'

    def __str__(self):
        return f'user: {self.username}'

    def generate_otp(self):
        return ''.join(random.choices(string.digits, k=OTP_LENGTH))

    def set_otp(self):
        otp = self.generate_otp()
        self.otp = otp
        type(self).objects.filter(id=self.id).update(otp=otp)

    def clear_otp(self):
        type(self).objects.filter(id=self.id).update(otp=None)

    def generate_token(self):
        return binascii.hexlify(os.urandom(20)).decode()

    def set_token(self):
        token = self.generate_token()
        cache.set(token, self.id)
        self.token = token
        type(self).objects.filter(id=self.id).update(token=token)

    def clear_token(self):
        cache.delete(self.token)
        type(self).objects.filter(id=self.id).update(token=None)
