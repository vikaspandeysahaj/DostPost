from django.db import models


class MasterPostType(models.Model):
    post_type = models.CharField(max_length=500, null=True, blank=True)
