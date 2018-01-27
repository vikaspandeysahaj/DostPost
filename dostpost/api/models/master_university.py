from django.db import models


class MasterUniversity(models.Model):
    university_name = models.CharField(max_length=255, unique=True)
