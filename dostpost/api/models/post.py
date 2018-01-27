from django.db import models

from api.models.master_post_type import MasterPostType
from api.models.user import User


class Post(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField(null=False, blank=False)
    media_link = models.CharField(max_length=500, null=True, blank=True)
    post_type = models.ForeignKey(MasterPostType, on_delete=models.CASCADE)


