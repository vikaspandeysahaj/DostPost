import json

from django.http import JsonResponse

from api.services.user_service import UserService


def get_user_list(request):
    if request.method == 'GET':
        page_number = int(request.GET.get('page', 1))
        page_size = 10
        total_page_count, json_data = UserService().get_user_list(page_size, page_number)
        context = {'results': json.loads(json_data), 'total_pages': total_page_count, 'current_page': page_number}
        return JsonResponse(context)

def get_user_profile(request, id):
    if request.method == 'GET':
        json_data = UserService().get_user_profile(user_id=id)
        context = {'results': json.loads(json_data)}
        return JsonResponse(context)