from rest_framework.generics import ListAPIView, RetrieveAPIView
from rest_framework.permissions import AllowAny
from django.template.response import TemplateResponse

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

    def get(self, request, *args, **kwargs):
        response = super().get(request, *args, **kwargs)
        return TemplateResponse(
            request=request,
            template='salons.html',
            context={'result': response.data}
        )


class SalonView(RetrieveAPIView):
    serializer_class = serializers.SalonSerializer
    permission_classes = [AllowAny]
    queryset = Salon.objects.all()

    def get(self, request, *args, **kwargs):
        response = super().get(request, *args, **kwargs)
        return TemplateResponse(
            request=request,
            template='salon.html',
            context={'salon': response.data}
        )


listsalon_view = ListSalonsView.as_view()
salon_view = SalonView.as_view()
