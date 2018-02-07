import json

from rest_framework.renderers import JSONRenderer

from api.handlers.master_company_model_handler import MasterCompanyModelHandler
from api.handlers.master_designation_model_handler import MasterDesignationModelHandler
from api.handlers.master_location_model_handler import MasterLocationModelHandler
from api.handlers.work_info_model_handler import WorkInfoModelHandler
from api.handlers.user_model_handler import UserModelHandler
from api.serializers.work_info_serializers import WorkInfoSerializer, MasterCompanySerializer, \
    MasterDesignationSerializer


class WorkService():

    def __init__(self, current_user):
        self.current_user = current_user

    def get_company_list(self):
        queryset = MasterCompanyModelHandler().find_all()
        data = MasterCompanySerializer(queryset, many=True).data
        json_data = JSONRenderer().render(data)
        return  json_data

    def get_designation_list(self):
        queryset = MasterDesignationModelHandler().find_all()
        data = MasterDesignationSerializer(queryset, many=True).data
        json_data = JSONRenderer().render(data)
        return  json_data

    def get_user_works(self, user_id):
        try:
            for_user = UserModelHandler().find_by_id(user_id)
            if for_user:
                queryset = WorkInfoModelHandler().find_by_user(for_user)
                data = WorkInfoSerializer(queryset, many=True).data
                json_data = JSONRenderer().render(data)
                return json_data
            else:
                return json.dumps({"Error":"User Not found"})
        except Exception as ex:
            return json.dumps({"Error":"Not able to fetch the works : %s"%(ex.message)})

    def add_user_work_info(self, work_json):
        try:
            company = MasterCompanyModelHandler().insert(company_name=work_json["company"])
            location = MasterLocationModelHandler().insert(location_name=work_json["location"])
            designation = MasterDesignationModelHandler().insert(designation_name=work_json["designation"])

            created_work_info = WorkInfoModelHandler().insert(
                user = self.current_user,
                company = company,
                location = location,
                designation=designation,
                start_date = work_json["start_date"],
                end_date = work_json["end_date"])

            data = WorkInfoSerializer(created_work_info).data
            json_data = JSONRenderer().render(data)
            return json_data
        except Exception as ex:
            return json.dumps({"Error":"Not able to add the work : %s"%(ex.message)})

    def remove_user_work_info(self, work_json):
        try:
            work_id = work_json["id"]
            deleted_work = WorkInfoModelHandler().remove(work_id, self.current_user)
            return json.dumps({"Sucess":"Work removed %s"%(deleted_work.id)})
        except Exception as ex:
            return json.dumps({"Error":"Not able to remove the work : %s"%(ex.message)})

    def update_user_work_info(self, work_json):
        try:
            company = MasterCompanyModelHandler().insert(company_name=work_json["company"])
            location = MasterLocationModelHandler().insert(location_name=work_json["location"])
            designation = MasterDesignationModelHandler().insert(designation_name=work_json["designation"])

            updated_work_info = WorkInfoModelHandler().update(
                id = work_json["id"],
                user = self.current_user,
                company = company,
                location = location,
                designation=designation,
                start_date = work_json["start_date"],
                end_date = work_json["end_date"])

            data = WorkInfoSerializer(updated_work_info).data
            json_data = JSONRenderer().render(data)
            return json_data
        except Exception as ex:
            return json.dumps({"Error":"Not able to update the work : %s"%(ex.message)})


