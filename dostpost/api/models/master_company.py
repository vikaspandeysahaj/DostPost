from django.db import models


class MasterCompany(models.Model):
    company_name = models.CharField(max_length=200, null=True, blank=True)
