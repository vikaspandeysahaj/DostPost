from django.db import models


class MasterUniversity(models.Model):
    university_name = models.CharField(max_length=500, null=True, blank=True)
