from rest_framework.fields import CharField
from rest_framework.serializers import ModelSerializer

from api.models import LocationInfo


class LocationInfoSerializer(ModelSerializer):
    location_name = CharField(source='location.location_name')
    class Meta:
        model = LocationInfo
        fields = ('id','location_name', 'when_start_date', 'when_end_date')


