from django.db import models

from api.models.master_public_site import MasterPublicSite
from api.models.user import User


class PublicProfileInfo(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    public_site = models.ForeignKey(MasterPublicSite, on_delete=models.CASCADE)
    url =  models.CharField(max_length=100, null=True, blank=True)

