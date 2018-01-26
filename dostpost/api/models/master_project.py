from django.db import models


class MasterProject(models.Model):
    project_name = models.CharField(max_length=500, null=True, blank=True)
