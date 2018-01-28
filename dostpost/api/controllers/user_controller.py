import json

from django.http import JsonResponse

from api.auth.user_auth import basic_auth_required, _CURRENT_USER
from api.services.user_service import UserService


@basic_auth_required
def get_user_list(request):
    if request.method == 'GET':
        current_user = request.user
        page_number = int(request.GET.get('page', 1))
        page_size = 10
        total_page_count, json_data = UserService(current_user).get_user_list(page_size, page_number)
        context = {'results': json.loads(json_data), 'total_pages': total_page_count, 'current_page': page_number}
        return JsonResponse(context)

@basic_auth_required
def get_user_profile(request, id):
    if request.method == 'GET':
        current_user = request.user
        json_data = UserService(current_user).get_user_profile(user_id=id)
        context = {'results': json.loads(json_data)}
        return JsonResponse(context)