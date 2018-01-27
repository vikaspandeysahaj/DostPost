from django.db import models


class MasterSkill(models.Model):
    skill_name = models.CharField(max_length=255, unique=True)
