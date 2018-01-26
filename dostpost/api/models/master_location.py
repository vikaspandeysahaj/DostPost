from django.db import models


class MasterLocation(models.Model):
    location_name = models.CharField(max_length=500, null=True, blank=True)
