from rest_framework.fields import CharField
from rest_framework.serializers import ModelSerializer

from api.models import PublicProfileInfo


class PublicProfileInfoSerializer(ModelSerializer):
    public_site = CharField(source='public_site.site_name')
    class Meta:
        model = PublicProfileInfo
        fields = ('id','public_site', 'url')


