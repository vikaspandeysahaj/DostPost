from django.core.paginator import Paginator
from rest_framework.renderers import JSONRenderer

from api.handlers.user_model_handler import UserModelHandler
from api.serializers.user_serializers import UserListSerializer, UserProfileSerializer


class UserService():

    def __init__(self, current_user):
        self.current_user = current_user

    def get_user_list(self, page_size = None, page_number = None):
        queryset = UserModelHandler().find_all()
        if page_size and page_number:
            paginator = Paginator(queryset, page_size)
            page = paginator.page(page_number)
            total_page_count = page.paginator.num_pages
            data = UserListSerializer(page, many=True).data
        else:
            data = UserListSerializer(queryset, many=True).data
            total_page_count = 1
        json_data = JSONRenderer().render(data)
        return total_page_count, json_data

    def get_user_profile(self, user_id):
        queryset = UserModelHandler().find_by_id(user_id)
        data = UserProfileSerializer(queryset).data
        json_data = JSONRenderer().render(data)
        return json_data
