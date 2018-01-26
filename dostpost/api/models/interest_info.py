from django.db import models

from api.models.master_company import MasterCompany
from api.models.master_designation import MasterDesignation
from api.models.master_interest import MasterInterest
from api.models.master_location import MasterLocation
from api.models.master_public_site import MasterPublicSite
from api.models.user import User


class InterestInfo(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    interest = models.ForeignKey(MasterInterest, on_delete=models.CASCADE)
    desc = models.CharField(max_length=1000, null=True, blank=True)

