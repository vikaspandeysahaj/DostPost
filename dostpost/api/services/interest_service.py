import json

from rest_framework.renderers import JSONRenderer

from api.handlers.master_location_model_handler import MasterLocationModelHandler
from api.handlers.master_interest_model_handler import MasterInterestModelHandler
from api.handlers.interest_info_model_handler import InterestInfoModelHandler
from api.handlers.user_model_handler import UserModelHandler
from api.serializers.interest_info_serializers import MasterInterestSerializer, InterestInfoSerializer


class InterestService():

    def __init__(self, current_user):
        self.current_user = current_user

    def get_interest_list(self):
        queryset = MasterInterestModelHandler().find_all()
        data = MasterInterestSerializer(queryset, many=True).data
        json_data = JSONRenderer().render(data)
        return  json_data

    def get_user_interests(self, user_id):
        try:
            for_user = UserModelHandler().find_by_id(user_id)
            if for_user:
                queryset = InterestInfoModelHandler().find_by_user(for_user)
                data = InterestInfoSerializer(queryset, many=True).data
                json_data = JSONRenderer().render(data)
                return json_data
            else:
                return json.dumps({"Error":"User Not found"})
        except Exception as ex:
            return json.dumps({"Error":"Not able to fetch the interests : %s"%(ex.message)})

    def add_user_interest_info(self, interest_json):
        try:
            interest = MasterInterestModelHandler().insert(interest_name=interest_json["interest"])

            created_interest_info = InterestInfoModelHandler().insert(
                user = self.current_user,
                interest = interest,
                desc = interest_json["desc"])

            data = InterestInfoSerializer(created_interest_info).data
            json_data = JSONRenderer().render(data)
            return json_data
        except Exception as ex:
            return json.dumps({"Error":"Not able to add the interest : %s"%(ex.message)})

    def remove_user_interest_info(self, interest_json):
        try:
            interest_id = interest_json["id"]
            deleted_interest = InterestInfoModelHandler().remove(interest_id, self.current_user)
            return json.dumps({"Sucess":"Interest removed %s"%(deleted_interest.id)})
        except Exception as ex:
            return json.dumps({"Error":"Not able to remove the interest : %s"%(ex.message)})

    def update_user_interest_info(self, interest_json):
        try:
            interest = MasterInterestModelHandler().insert(interest_name=interest_json["interest"])

            updated_interest_info = InterestInfoModelHandler().update(
                id = interest_json["id"],
                user = self.current_user,
                interest = interest,
                desc = interest_json["desc"])

            data = InterestInfoSerializer(updated_interest_info).data
            json_data = JSONRenderer().render(data)
            return json_data
        except Exception as ex:
            return json.dumps({"Error":"Not able to update the interest : %s"%(ex.message)})


