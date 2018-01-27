from django.db import models


class MasterPublicSite(models.Model):
    site_name = models.CharField(max_length=255, unique=True)
