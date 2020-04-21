from rest_framework.serializers import ModelSerializer
from salon.models import Salon


class SalonSerializer(ModelSerializer):
    class Meta:
        model = Salon
        fields = ('id', 'name')
        readonly_field = ('id',)

