from django.db import models

from api.models.master_location import MasterLocation
from api.models.user import User


class ContactInfo(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    location = models.ForeignKey(MasterLocation, on_delete=models.CASCADE)
    email = models.EmailField(null=True, blank=True)
    phone = models.CharField(max_length=10, null=True, blank=True)
    mobile = models.CharField(max_length=10, null=True, blank=True)
    address = models.CharField(max_length=500, null=True, blank=True)



