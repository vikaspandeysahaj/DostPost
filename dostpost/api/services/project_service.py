import json

from rest_framework.renderers import JSONRenderer

from api.handlers.master_location_model_handler import MasterLocationModelHandler
from api.handlers.master_project_model_handler import MasterProjectModelHandler
from api.handlers.project_info_model_handler import ProjectInfoModelHandler
from api.handlers.user_model_handler import UserModelHandler
from api.serializers.project_info_serializers import MasterProjectSerializer, ProjectInfoSerializer


class ProjectService():

    def __init__(self, current_user):
        self.current_user = current_user

    def get_project_list(self):
        queryset = MasterProjectModelHandler().find_all()
        data = MasterProjectSerializer(queryset, many=True).data
        json_data = JSONRenderer().render(data)
        return  json_data

    def get_user_projects(self, user_id):
        try:
            for_user = UserModelHandler().find_by_id(user_id)
            if for_user:
                queryset = ProjectInfoModelHandler().find_by_user(for_user)
                data = ProjectInfoSerializer(queryset, many=True).data
                json_data = JSONRenderer().render(data)
                return json_data
            else:
                return json.dumps({"Error":"User Not found"})
        except Exception as ex:
            return json.dumps({"Error":"Not able to fetch the projects : %s"%(ex.message)})

    def add_user_project_info(self, project_json):
        try:
            location = MasterLocationModelHandler().insert(location_name=project_json["location"])
            project = MasterProjectModelHandler().insert(project_name=project_json["project"])

            created_project_info = ProjectInfoModelHandler().insert(
                user = self.current_user,
                project = project,
                location = location,
                start_date = project_json["start_date"],
                end_date = project_json["end_date"])

            data = ProjectInfoSerializer(created_project_info).data
            json_data = JSONRenderer().render(data)
            return json_data
        except Exception as ex:
            return json.dumps({"Error":"Not able to add the project : %s"%(ex.message)})

    def remove_user_project_info(self, project_json):
        try:
            project_id = project_json["id"]
            deleted_project = ProjectInfoModelHandler().remove(project_id, self.current_user)
            return json.dumps({"Sucess":"Project removed %s"%(deleted_project.id)})
        except Exception as ex:
            return json.dumps({"Error":"Not able to remove the project : %s"%(ex.message)})

    def update_user_project_info(self, project_json):
        try:
            location = MasterLocationModelHandler().insert(location_name=project_json["location"])
            project = MasterProjectModelHandler().insert(project_name=project_json["project"])

            updated_project_info = ProjectInfoModelHandler().update(
                id = project_json["id"],
                user = self.current_user,
                project = project,
                location = location,
                start_date = project_json["start_date"],
                end_date = project_json["end_date"])

            data = ProjectInfoSerializer(updated_project_info).data
            json_data = JSONRenderer().render(data)
            return json_data
        except Exception as ex:
            return json.dumps({"Error":"Not able to update the project : %s"%(ex.message)})


