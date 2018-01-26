from django.db import models

from api.models.master_location import MasterLocation
from api.models.user import User


class LocationInfo(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    location = models.ForeignKey(MasterLocation, on_delete=models.CASCADE)
    when_start_date = models.CharField(max_length=50, null=True, blank=True)
    when_end_date = models.CharField(max_length=50, null=True, blank=True)

