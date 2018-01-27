from django.db import models

from api.models.master_notification_type import MasterNotificationType
from api.models.user import User


class Notification(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    notification = models.CharField(max_length=500, null=True, blank=True)
    notification_type = models.ForeignKey(MasterNotificationType, on_delete=models.CASCADE)


