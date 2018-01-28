from rest_framework.fields import CharField
from rest_framework.serializers import ModelSerializer

from api.models import ProjectInfo, MasterProject


class MasterProjectSerializer(ModelSerializer):
    class Meta:
        model = MasterProject
        fields = ('id','project_name')


class ProjectInfoSerializer(ModelSerializer):
    project = CharField(source='project.project_name')
    location = CharField(source='location.location_name')
    class Meta:
        model = ProjectInfo
        fields = ('id','project', 'location', 'start_date', 'end_date')


