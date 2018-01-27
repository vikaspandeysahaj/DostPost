from django.db import models


class MasterCompany(models.Model):
    company_name = models.CharField(max_length=255, unique=True)
