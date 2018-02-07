import json

from rest_framework.renderers import JSONRenderer

from api.handlers.master_location_model_handler import MasterLocationModelHandler
from api.handlers.contact_info_model_handler import ContactInfoModelHandler
from api.handlers.user_model_handler import UserModelHandler
from api.serializers.contact_info_serializers import ContactInfoSerializer


class ContactService():

    def __init__(self, current_user):
        self.current_user = current_user

    def get_user_contact_info(self, user_id):
        try:
            for_user = UserModelHandler().find_by_id(user_id)
            if for_user:
                queryset = ContactInfoModelHandler().find_by_user(for_user)
                data = ContactInfoSerializer(queryset).data
                json_data = JSONRenderer().render(data)
                return json_data
            else:
                return json.dumps({"Error":"User Not found"})
        except Exception as ex:
            return json.dumps({"Error":"Not able to fetch the contacts : %s"%(ex.message)})

    def add_user_contact_info(self, contact_json):
        try:
            location = MasterLocationModelHandler().insert(location_name=contact_json["location"])
            created_contact_info = ContactInfoModelHandler().insert(
                user = self.current_user,
                location = location,
                email = contact_json["email"],
                phone = contact_json["phone"],
                mobile = contact_json["mobile"],
                address = contact_json["address"])

            data = ContactInfoSerializer(created_contact_info).data
            json_data = JSONRenderer().render(data)
            return json_data
        except Exception as ex:
            return json.dumps({"Error":"Not able to add the contact : %s"%(ex.message)})

    def update_user_contact_info(self, contact_json):
        try:
            location = MasterLocationModelHandler().insert(location_name=contact_json["location"])
            updated_contact_info = ContactInfoModelHandler().update(
                id = contact_json["id"],
                user = self.current_user,
                location = location,
                email = contact_json["email"],
                phone = contact_json["phone"],
                mobile = contact_json["mobile"],
                address = contact_json["address"])
            data = ContactInfoSerializer(updated_contact_info).data
            json_data = JSONRenderer().render(data)
            return json_data
        except Exception as ex:
            return json.dumps({"Error":"Not able to update the contact : %s"%(ex.message)})


