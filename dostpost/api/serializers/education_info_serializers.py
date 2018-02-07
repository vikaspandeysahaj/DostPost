from rest_framework.fields import CharField
from rest_framework.serializers import ModelSerializer

from api.models import EducationInfo, MasterUniversity


class MasterUniversitySerializer(ModelSerializer):
    class Meta:
        model = MasterUniversity
        fields = ('id','university_name')


class EducationInfoSerializer(ModelSerializer):
    location = CharField(source='location.location_name')
    university= CharField(source='university.university_name')
    education_type = CharField(source='education_type.education_type')
    class Meta:
        model = EducationInfo
        fields = ('id','location', 'university','education_type', 'start_date', 'end_date')


