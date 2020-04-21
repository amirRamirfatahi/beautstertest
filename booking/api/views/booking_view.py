from rest_framework.generics import CreateAPIView
from django.views.generic import TemplateView

from booking.api import serializers
from booking.models import Booking

class BookingView(CreateAPIView, TemplateView):
    serializer_class = serializers.BookingSerializer
    queryset = Booking.objects.all()

    def perform_create(self, serializer):
        serializer.save(**{'user_id': self.request.user.id})


booking_view = BookingView.as_view()
