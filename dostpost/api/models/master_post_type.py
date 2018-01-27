from django.db import models


class MasterPostType(models.Model):
    post_type = models.CharField(max_length=255, unique=True)
