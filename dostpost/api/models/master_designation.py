from django.db import models


class MasterDesignation(models.Model):
    designation_name = models.CharField(max_length=255, unique=True)
