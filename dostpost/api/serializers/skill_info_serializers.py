from rest_framework.fields import CharField
from rest_framework.serializers import ModelSerializer

from api.models import SkillInfo, MasterSkill


class MasterSkillSerializer(ModelSerializer):
    class Meta:
        model = MasterSkill
        fields = ('id','skill_name')

class SkillInfoSerializer(ModelSerializer):
    skill = CharField(source='skill.skill_name')
    class Meta:
        model = SkillInfo
        fields = ('id','skill', 'rank')


