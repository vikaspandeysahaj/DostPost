from django.db import models

from api.models.master_company import MasterCompany
from api.models.master_designation import MasterDesignation
from api.models.master_location import MasterLocation
from api.models.user import User


class WorkInfo(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    company = models.ForeignKey(MasterCompany, on_delete=models.CASCADE)
    location = models.ForeignKey(MasterLocation, on_delete=models.CASCADE)
    designation = models.ForeignKey(MasterDesignation, on_delete=models.CASCADE)
    start_date = models.CharField(max_length=50, null=True, blank=True)
    end_date = models.CharField(max_length=50, null=True, blank=True)

