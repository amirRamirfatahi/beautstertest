from rest_framework.generics import ListAPIView
from rest_framework.permissions import AllowAny

from salon.models import Salon
from salon.api import serializers
from salon.utils import filters


class ListSalonsView(ListAPIView):
    serializer_class = serializers.SalonSerializer
    permission_classes = [AllowAny]
    queryset = Salon.objects.all()
    filter_backends = [filters.TrigramSearchFilterBackend]
    tgsearch_field = 'name'
    tgsearch_threshold = 0.1


listsalon_view = ListSalonsView.as_view()
