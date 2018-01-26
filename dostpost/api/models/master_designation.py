from django.db import models


class MasterDesignation(models.Model):
    designation_name = models.CharField(max_length=500, null=True, blank=True)
