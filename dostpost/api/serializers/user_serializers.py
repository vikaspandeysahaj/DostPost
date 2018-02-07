from rest_framework.fields import CharField, SerializerMethodField
from rest_framework.renderers import JSONRenderer
from rest_framework.serializers import ModelSerializer

from api.models import User
from api.serializers.contact_info_serializers import ContactInfoSerializer
from api.serializers.education_info_serializers import EducationInfoSerializer
from api.serializers.interest_info_serializers import InterestInfoSerializer
from api.serializers.location_info_serializers import LocationInfoSerializer
from api.serializers.project_info_serializers import ProjectInfoSerializer
from api.serializers.public_profile_info_serializers import PublicProfileInfoSerializer
from api.serializers.salary_info_serializers import SalaryInfoSerializer
from api.serializers.skill_info_serializers import SkillInfoSerializer
from api.serializers.work_info_serializers import WorkInfoSerializer


class UserListSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'employee_id','full_name', 'first_name', 'middle_name', 'last_name')


class UserProfileSerializer(ModelSerializer):
    marital_status = CharField(source='marital_status.status')
    location_info = SerializerMethodField()
    contact_info = SerializerMethodField()
    eduction_info = SerializerMethodField()
    interest_info = SerializerMethodField()
    project_info = SerializerMethodField()
    salary_info = SerializerMethodField()
    skill_info = SerializerMethodField()
    work_info = SerializerMethodField()
    public_profile_info = SerializerMethodField()

    def get_location_info(self, user):
        data = LocationInfoSerializer(user.locationinfo_set.all(), many=True).data
        return data

    def get_public_profile_info(self, user):
        data = PublicProfileInfoSerializer(user.publicprofileinfo_set.all(), many=True).data
        return data

    def get_contact_info(self, user):
        data = ContactInfoSerializer(user.contactinfo_set.first()).data
        return data

    def get_eduction_info(self, user):
        data = EducationInfoSerializer(user.educationinfo_set.all(), many=True).data
        return data

    def get_interest_info(self, user):
        data = InterestInfoSerializer(user.interestinfo_set.all(), many=True).data
        return data

    def get_project_info(self, user):
        data = ProjectInfoSerializer(user.projectinfo_set.all(), many=True).data
        return data

    def get_salary_info(self, user):
        data = SalaryInfoSerializer(user.salaryinfo_set.first()).data
        return data

    def get_skill_info(self, user):
        data = SkillInfoSerializer(user.skillinfo_set.all(), many=True).data
        return data

    def get_work_info(self, user):
        data = WorkInfoSerializer(user.workinfo_set.all(), many=True).data
        return data

    class Meta:
        model = User
        fields = ('id', 'employee_id','full_name', 'first_name', 'middle_name',
                  'last_name', 'DOB', 'Gender', 'marital_status', 'location_info',
                  'contact_info', 'eduction_info', 'interest_info', 'project_info', 'salary_info',
                  'skill_info', 'work_info', 'public_profile_info')