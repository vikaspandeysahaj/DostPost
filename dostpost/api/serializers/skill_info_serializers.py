from rest_framework.fields import CharField
from rest_framework.serializers import ModelSerializer

from api.models import SkillInfo


class SkillInfoSerializer(ModelSerializer):
    skill = CharField(source='skill.skill_name')
    class Meta:
        model = SkillInfo
        fields = ('id','skill', 'rank')


