from rest_framework.serializers import ModelSerializer

from booking.models import Booking


class BookingSerializer(ModelSerializer):
    class Meta:
        model = Booking
        exclude = ('id',)
        extra_kwargs = {'user': {'read_only': True}}

