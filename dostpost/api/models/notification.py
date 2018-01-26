from django.db import models

from api.models.master_location import MasterLocation
from api.models.master_notification import MasterNotification
from api.models.master_post_type import MasterPostType
from api.models.post import Post
from api.models.user import User


class Notification(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    notification = models.CharField(max_length=500, null=True, blank=True)
    notification_type = models.ForeignKey(MasterNotification, on_delete=models.CASCADE)


