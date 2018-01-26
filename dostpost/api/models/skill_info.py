from django.db import models

from api.models.master_skill import MasterSkill
from api.models.user import User


class SkillInfo(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    skill = models.ForeignKey(MasterSkill, on_delete=models.CASCADE)
    rank = models.IntegerField(null=True, blank=True)



