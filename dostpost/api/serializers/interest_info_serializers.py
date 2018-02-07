from rest_framework.fields import CharField
from rest_framework.serializers import ModelSerializer

from api.models import InterestInfo, MasterInterest


class MasterInterestSerializer(ModelSerializer):
    class Meta:
        model = MasterInterest
        fields = ('id','interest_name')

class InterestInfoSerializer(ModelSerializer):
    interest = CharField(source='interest.interest_name')
    class Meta:
        model = InterestInfo
        fields = ('id','interest', 'desc')


