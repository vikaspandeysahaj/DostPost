from django.db import models


class MasterInterest(models.Model):
    interest_name = models.CharField(max_length=255, unique=True)
