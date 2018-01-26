from django.db import models

from api.models.user import User


class SalaryInfo(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    salary = models.IntegerField(null=True, blank=True)
    revised_date = models.CharField(max_length=50, null=True, blank=True)



