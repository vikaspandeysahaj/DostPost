from rest_framework.fields import CharField
from rest_framework.serializers import ModelSerializer

from api.models import WorkInfo


class WorkInfoSerializer(ModelSerializer):
    company = CharField(source='company.company_name')
    location = CharField(source='location.location_name')
    designation = CharField(source='designation.designation_name')
    class Meta:
        model = WorkInfo
        fields = ('id','company','location', 'designation','start_date', 'end_date')


