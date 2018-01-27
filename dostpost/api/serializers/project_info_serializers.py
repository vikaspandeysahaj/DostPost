from rest_framework.fields import CharField
from rest_framework.serializers import ModelSerializer

from api.models import ProjectInfo


class ProjectInfoSerializer(ModelSerializer):
    project = CharField(source='project.project_name')
    location_name = CharField(source='location.location_name')
    class Meta:
        model = ProjectInfo
        fields = ('id','project', 'location_name', 'start_date', 'end_date')


