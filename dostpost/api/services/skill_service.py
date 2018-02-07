import json

from rest_framework.renderers import JSONRenderer
from api.handlers.master_skill_model_handler import MasterSkillModelHandler
from api.handlers.skill_info_model_handler import SkillInfoModelHandler
from api.handlers.user_model_handler import UserModelHandler
from api.serializers.skill_info_serializers import MasterSkillSerializer, SkillInfoSerializer


class SkillService():

    def __init__(self, current_user):
        self.current_user = current_user

    def get_skill_list(self):
        queryset = MasterSkillModelHandler().find_all()
        data = MasterSkillSerializer(queryset, many=True).data
        json_data = JSONRenderer().render(data)
        return  json_data

    def get_user_skills(self, user_id):
        try:
            for_user = UserModelHandler().find_by_id(user_id)
            if for_user:
                queryset = SkillInfoModelHandler().find_by_user(for_user)
                data = SkillInfoSerializer(queryset, many=True).data
                json_data = JSONRenderer().render(data)
                return json_data
            else:
                return json.dumps({"Error":"User Not found"})
        except Exception as ex:
            return json.dumps({"Error":"Not able to fetch the skills : %s"%(ex.message)})

    def add_user_skill_info(self, skill_json):
        try:
            skill = MasterSkillModelHandler().insert(skill_name=skill_json["skill"])

            created_skill_info = SkillInfoModelHandler().insert(
                user = self.current_user,
                skill = skill,
                rank = skill_json["rank"])

            data = SkillInfoSerializer(created_skill_info).data
            json_data = JSONRenderer().render(data)
            return json_data
        except Exception as ex:
            return json.dumps({"Error":"Not able to add the skill : %s"%(ex.message)})

    def remove_user_skill_info(self, skill_json):
        try:
            skill_id = skill_json["id"]
            deleted_skill = SkillInfoModelHandler().remove(skill_id, self.current_user)
            return json.dumps({"Sucess":"Skill removed %s"%(deleted_skill.id)})
        except Exception as ex:
            return json.dumps({"Error":"Not able to remove the skill : %s"%(ex.message)})

    def update_user_skill_info(self, skill_json):
        try:
            skill = MasterSkillModelHandler().insert(skill_name=skill_json["skill"])

            updated_skill_info = SkillInfoModelHandler().update(
                id = skill_json["id"],
                user = self.current_user,
                skill = skill,
                rank = skill_json["rank"])

            data = SkillInfoSerializer(updated_skill_info).data
            json_data = JSONRenderer().render(data)
            return json_data
        except Exception as ex:
            return json.dumps({"Error":"Not able to update the skill : %s"%(ex.message)})


