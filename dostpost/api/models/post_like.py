from django.db import models

from api.models.master_location import MasterLocation
from api.models.master_post_type import MasterPostType
from api.models.post import Post
from api.models.user import User


class PostLike(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)


