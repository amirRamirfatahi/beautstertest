from django.contrib import admin

from salon.models import Salon


class SalonAdmin(admin.ModelAdmin):
    pass

admin.site.register(Salon, SalonAdmin)
