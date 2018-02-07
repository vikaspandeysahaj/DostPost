from rest_framework.fields import CharField
from rest_framework.serializers import ModelSerializer

from api.models import LocationInfo, MasterLocation


class MasterLocationSerializer(ModelSerializer):
    class Meta:
        model = MasterLocation
        fields = ('id','location_name')

class LocationInfoSerializer(ModelSerializer):
    location = CharField(source='location.location_name')
    class Meta:
        model = LocationInfo
        fields = ('id','location', 'when_start_date', 'when_end_date')


