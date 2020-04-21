from django.db import models
from django.conf import settings


class Booking(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL,
                             on_delete=models.CASCADE)
    salon = models.ForeignKey('salon.Salon', on_delete=models.CASCADE)

    def __str__(self):
        return f'for {self.user_id} with {self.salon_id}'
