from django.db import models

from api.models.master_education_type import MasterEducationType
from api.models.master_location import MasterLocation
from api.models.master_university import MasterUniversity
from api.models.user import User


class EducationInfo(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    university = models.ForeignKey(MasterUniversity, on_delete=models.CASCADE)
    location = models.ForeignKey(MasterLocation, on_delete=models.CASCADE)
    education_type = models.ForeignKey(MasterEducationType, on_delete=models.CASCADE)
    start_date = models.CharField(max_length=50, null=True, blank=True)
    end_date = models.CharField(max_length=50, null=True, blank=True)

