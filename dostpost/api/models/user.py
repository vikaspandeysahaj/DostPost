from django.db import models

from api.models.master_marital_status import MasterMaritalStatus


class User(models.Model):
    full_name = models.CharField(max_length=50, null=True, blank=True)
    first_name = models.CharField(max_length=50, null=True, blank=True)
    middle_name = models.CharField(max_length=50, null=True, blank=True)
    last_name = models.CharField(max_length=50, null=True, blank=True)
    DOB = models.CharField(max_length=50, null=True, blank=True)
    Gender = models.CharField(max_length=50, null=True, blank=True)
    marital_status = models.ForeignKey(MasterMaritalStatus, on_delete=models.CASCADE)