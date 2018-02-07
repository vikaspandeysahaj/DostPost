import json

from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

from api.auth.user_auth import basic_auth_required, _CURRENT_USER
from api.services.interest_service import InterestService


@basic_auth_required
def get_interest_list(request):
    if request.method == 'GET':
        current_user = request.user
        json_data = InterestService(current_user).get_interest_list()
        context = {'results': json.loads(json_data)}
        return JsonResponse(context)

@basic_auth_required
def get_user_interest_info(request, id):
    if request.method == 'GET':
        current_user = request.user
        json_data = InterestService(current_user).get_user_interests(id)
        context = {'results': json.loads(json_data)}
        return JsonResponse(context)


@basic_auth_required
@csrf_exempt
def add_user_interest_info(request):
    if request.method == 'POST':
        current_user = request.user
        interest_json = json.loads(request.body)
        json_data = InterestService(current_user).add_user_interest_info(interest_json = interest_json)
        context = {'results': json.loads(json_data)}
        return JsonResponse(context)

@basic_auth_required
@csrf_exempt
def remove_user_interest_info(request):
    if request.method == 'POST':
        current_user = request.user
        interest_json = json.loads(request.body)
        json_data = InterestService(current_user).remove_user_interest_info(interest_json = interest_json)
        context = {'results': json.loads(json_data)}
        return JsonResponse(context)

@basic_auth_required
@csrf_exempt
def update_user_interest_info(request):
    if request.method == 'POST':
        current_user = request.user
        interest_json = json.loads(request.body)
        json_data = InterestService(current_user).update_user_interest_info(interest_json = interest_json)
        context = {'results': json.loads(json_data)}
        return JsonResponse(context)