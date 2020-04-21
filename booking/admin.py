from django.contrib import admin

from booking.models import Booking


class BookingAdmin(admin.ModelAdmin):
    pass


admin.site.register(Booking, BookingAdmin)
