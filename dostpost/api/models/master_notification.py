from django.db import models


class MasterNotification(models.Model):
    notification_name = models.CharField(max_length=100, null=True, blank=True)
