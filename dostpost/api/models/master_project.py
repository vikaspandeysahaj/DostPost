from django.db import models


class MasterProject(models.Model):
    project_name = models.CharField(max_length=255, unique=True)
