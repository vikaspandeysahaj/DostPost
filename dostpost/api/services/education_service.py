import json

from rest_framework.renderers import JSONRenderer

from api.handlers.master_education_model_handler import MasterEducationTypeModelHandler
from api.handlers.master_location_model_handler import MasterLocationModelHandler
from api.handlers.education_info_model_handler import EducationInfoModelHandler
from api.handlers.master_university_model_handler import MasterUniversityModelHandler
from api.handlers.user_model_handler import UserModelHandler
from api.serializers.education_info_serializers import EducationInfoSerializer, MasterUniversitySerializer


class EducationService():

    def __init__(self, current_user):
        self.current_user = current_user

    def get_university_list(self):
        queryset = MasterUniversityModelHandler().find_all()
        data = MasterUniversitySerializer(queryset, many=True).data
        json_data = JSONRenderer().render(data)
        return  json_data

    def get_user_educations(self, user_id):
        try:
            for_user = UserModelHandler().find_by_id(user_id)
            if for_user:
                queryset = EducationInfoModelHandler().find_by_user(for_user)
                data = EducationInfoSerializer(queryset, many=True).data
                json_data = JSONRenderer().render(data)
                return json_data
            else:
                return json.dumps({"Error":"User Not found"})
        except Exception as ex:
            return json.dumps({"Error":"Not able to fetch the educations : %s"%(ex.message)})

    def add_user_education_info(self, education_json):
        try:
            location = MasterLocationModelHandler().insert(location_name=education_json["location"])
            university = MasterUniversityModelHandler().insert(university_name=education_json["university"])
            education_type = MasterEducationTypeModelHandler().insert(education_type=education_json["education_type"])

            created_education_info = EducationInfoModelHandler().insert(
                user = self.current_user,
                university = university,
                location = location,
                education_type = education_type,
                start_date = education_json["start_date"],
                end_date = education_json["end_date"])

            data = EducationInfoSerializer(created_education_info).data
            json_data = JSONRenderer().render(data)
            return json_data
        except Exception as ex:
            return json.dumps({"Error":"Not able to add the education : %s"%(ex.message)})

    def remove_user_education_info(self, education_json):
        try:
            education_id = education_json["id"]
            deleted_education = EducationInfoModelHandler().remove(education_id, self.current_user)
            return json.dumps({"Sucess":"Education removed %s"%(deleted_education.id)})
        except Exception as ex:
            return json.dumps({"Error":"Not able to remove the education : %s"%(ex.message)})

    def update_user_education_info(self, education_json):
        try:
            location = MasterLocationModelHandler().insert(location_name=education_json["location"])
            university = MasterUniversityModelHandler().insert(university_name=education_json["university"])
            education_type = MasterEducationTypeModelHandler().insert(education_type=education_json["education_type"])

            updated_education_info = EducationInfoModelHandler().update(
                id = education_json["id"],
                user = self.current_user,
                university = university,
                location = location,
                education_type = education_type,
                start_date = education_json["start_date"],
                end_date = education_json["end_date"])

            data = EducationInfoSerializer(updated_education_info).data
            json_data = JSONRenderer().render(data)
            return json_data
        except Exception as ex:
            return json.dumps({"Error":"Not able to update the education : %s"%(ex.message)})


