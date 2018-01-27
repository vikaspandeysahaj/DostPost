from django.db import models

from api.models import MasterLocation
from api.models.master_project import MasterProject
from api.models.user import User


class ProjectInfo(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    project = models.ForeignKey(MasterProject, on_delete=models.CASCADE)
    location = models.ForeignKey(MasterLocation, on_delete=models.CASCADE)
    start_date = models.CharField(max_length=50, null=True, blank=True)
    end_date = models.CharField(max_length=50, null=True, blank=True)



