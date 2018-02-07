import json

from rest_framework.renderers import JSONRenderer

from api.handlers.master_public_site_model_handler import MasterPublicSiteModelHandler
from api.handlers.public_profile_info_model_handler import PublicProfileInfoModelHandler
from api.handlers.user_model_handler import UserModelHandler
from api.serializers.public_profile_info_serializers import PublicProfileInfoSerializer, MasterPublicSiteSerializer


class PublicProfileService():

    def __init__(self, current_user):
        self.current_user = current_user

    def get_public_site_list(self):
        queryset = MasterPublicSiteModelHandler().find_all()
        data = MasterPublicSiteSerializer(queryset, many=True).data
        json_data = JSONRenderer().render(data)
        return  json_data

    def get_user_public_profiles(self, user_id):
        try:
            for_user = UserModelHandler().find_by_id(user_id)
            if for_user:
                queryset = PublicProfileInfoModelHandler().find_by_user(for_user)
                data = PublicProfileInfoSerializer(queryset, many=True).data
                json_data = JSONRenderer().render(data)
                return json_data
            else:
                return json.dumps({"Error":"User Not found"})
        except Exception as ex:
            return json.dumps({"Error":"Not able to fetch the public_profiles : %s"%(ex.message)})

    def add_user_public_profile_info(self, public_profile_json):
        try:

            public_site = MasterPublicSiteModelHandler().insert(site_name=public_profile_json["site"])

            created_public_profile_info = PublicProfileInfoModelHandler().insert(
                user = self.current_user,
                public_site = public_site,
                url = public_profile_json["url"])

            data = PublicProfileInfoSerializer(created_public_profile_info).data
            json_data = JSONRenderer().render(data)
            return json_data
        except Exception as ex:
            return json.dumps({"Error":"Not able to add the public_profile : %s"%(ex.message)})

    def remove_user_public_profile_info(self, public_profile_json):
        try:
            public_profile_id = public_profile_json["id"]
            deleted_public_profile = PublicProfileInfoModelHandler().remove(public_profile_id, self.current_user)
            return json.dumps({"Sucess":"PublicProfile removed %s"%(deleted_public_profile.id)})
        except Exception as ex:
            return json.dumps({"Error":"Not able to remove the public_profile : %s"%(ex.message)})

    def update_user_public_profile_info(self, public_profile_json):
        try:
            public_site = MasterPublicSiteModelHandler().insert(site_name=public_profile_json["site"])
            updated_public_profile_info = PublicProfileInfoModelHandler().update(
                id = public_profile_json["id"],
                user = self.current_user,
                public_site = public_site,
                url = public_profile_json["url"])

            data = PublicProfileInfoSerializer(updated_public_profile_info).data
            json_data = JSONRenderer().render(data)
            return json_data
        except Exception as ex:
            return json.dumps({"Error":"Not able to update the public_profile : %s"%(ex.message)})


