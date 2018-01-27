from rest_framework.fields import CharField
from rest_framework.serializers import ModelSerializer

from api.models import SalaryInfo


class SalaryInfoSerializer(ModelSerializer):
    class Meta:
        model = SalaryInfo
        fields = ('id','salary', 'revised_date')


