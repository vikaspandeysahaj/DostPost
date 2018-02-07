from rest_framework.fields import CharField
from rest_framework.serializers import ModelSerializer

from api.models import WorkInfo, MasterCompany, MasterDesignation


class MasterCompanySerializer(ModelSerializer):
    class Meta:
        model = MasterCompany
        fields = ('id','company_name')

class MasterDesignationSerializer(ModelSerializer):
    class Meta:
        model = MasterDesignation
        fields = ('id','designation_name')

class WorkInfoSerializer(ModelSerializer):
    company = CharField(source='company.company_name')
    location = CharField(source='location.location_name')
    designation = CharField(source='designation.designation_name')
    class Meta:
        model = WorkInfo
        fields = ('id','company','location', 'designation','start_date', 'end_date')


