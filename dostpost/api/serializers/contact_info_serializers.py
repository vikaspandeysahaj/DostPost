from rest_framework.fields import CharField
from rest_framework.serializers import ModelSerializer

from api.models import ContactInfo


class ContactInfoSerializer(ModelSerializer):
    location = CharField(source='location.location_name')
    class Meta:
        model = ContactInfo
        fields = ('id','location', 'email', 'phone', 'mobile', 'address')


