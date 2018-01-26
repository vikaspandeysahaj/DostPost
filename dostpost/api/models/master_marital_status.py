from django.db import models


class MasterMaritalStatus(models.Model):
    status = models.CharField(max_length=500, null=True, blank=True)
