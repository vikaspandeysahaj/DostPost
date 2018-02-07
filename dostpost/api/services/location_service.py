import json

from rest_framework.renderers import JSONRenderer

from api.handlers.master_location_model_handler import MasterLocationModelHandler
from api.handlers.location_info_model_handler import LocationInfoModelHandler
from api.handlers.user_model_handler import UserModelHandler
from api.serializers.location_info_serializers import MasterLocationSerializer, LocationInfoSerializer


class LocationService():

    def __init__(self, current_user):
        self.current_user = current_user

    def get_location_list(self):
        queryset = MasterLocationModelHandler().find_all()
        data = MasterLocationSerializer(queryset, many=True).data
        json_data = JSONRenderer().render(data)
        return  json_data

    def get_user_locations(self, user_id):
        try:
            for_user = UserModelHandler().find_by_id(user_id)
            if for_user:
                queryset = LocationInfoModelHandler().find_by_user(for_user)
                data = LocationInfoSerializer(queryset, many=True).data
                json_data = JSONRenderer().render(data)
                return json_data
            else:
                return json.dumps({"Error":"User Not found"})
        except Exception as ex:
            return json.dumps({"Error":"Not able to fetch the locations : %s"%(ex.message)})

    def add_user_location_info(self, location_json):
        try:
            location = MasterLocationModelHandler().insert(location_name=location_json["location"])
            created_location_info = LocationInfoModelHandler().insert(
                user = self.current_user,
                location = location,
                when_start_date = location_json["when_start_date"],
                when_end_date = location_json["when_end_date"])

            data = LocationInfoSerializer(created_location_info).data
            json_data = JSONRenderer().render(data)
            return json_data
        except Exception as ex:
            return json.dumps({"Error":"Not able to add the location : %s"%(ex.message)})

    def remove_user_location_info(self, location_json):
        try:
            location_id = location_json["id"]
            deleted_location = LocationInfoModelHandler().remove(location_id, self.current_user)
            return json.dumps({"Sucess":"Location removed %s"%(deleted_location.id)})
        except Exception as ex:
            return json.dumps({"Error":"Not able to remove the location : %s"%(ex.message)})

    def update_user_location_info(self, location_json):
        try:
            location = MasterLocationModelHandler().insert(location_name=location_json["location"])

            updated_location_info = LocationInfoModelHandler().update(
                id = location_json["id"],
                user = self.current_user,
                location = location,
                when_start_date = location_json["when_start_date"],
                when_end_date = location_json["when_end_date"])

            data = LocationInfoSerializer(updated_location_info).data
            json_data = JSONRenderer().render(data)
            return json_data
        except Exception as ex:
            return json.dumps({"Error":"Not able to update the location : %s"%(ex.message)})


