import string
import random

from django.contrib.auth.models import AbstractBaseUser
from django.db import models

from authenti.constants import OTP_LENGTH


class User(AbstractBaseUser):
    username = models.CharField(max_length=150, unique=True)
    email = models.EmailField(unique=True)
    otp = models.CharField(max_length=OTP_LENGTH, blank=True, null=True)

    USERNAME_FIELD = 'username'

    def __str__(self):
        return f'user: {self.username}'

    def generate_otp(self):
        return ''.join(random.choices(string.digits, k=OTP_LENGTH))

    def set_otp(self):
        self.objects.filter(id=self.id).update(otp=otp)

    def clear_otp(self):
        self.objects.filter(id=self.id).update(otp=null)

