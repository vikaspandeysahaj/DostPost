from django.db import models


class MasterNotificationType(models.Model):
    notification_name = models.CharField(max_length=100, unique=True)
