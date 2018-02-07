import json

from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

from api.auth.user_auth import basic_auth_required, _CURRENT_USER
from api.services.location_service import LocationService


@basic_auth_required
def get_location_list(request):
    if request.method == 'GET':
        current_user = request.user
        json_data = LocationService(current_user).get_location_list()
        context = {'results': json.loads(json_data)}
        return JsonResponse(context)

@basic_auth_required
def get_user_location_info(request, id):
    if request.method == 'GET':
        current_user = request.user
        json_data = LocationService(current_user).get_user_locations(id)
        context = {'results': json.loads(json_data)}
        return JsonResponse(context)


@basic_auth_required
@csrf_exempt
def add_user_location_info(request):
    if request.method == 'POST':
        current_user = request.user
        location_json = json.loads(request.body)
        json_data = LocationService(current_user).add_user_location_info(location_json = location_json)
        context = {'results': json.loads(json_data)}
        return JsonResponse(context)

@basic_auth_required
@csrf_exempt
def remove_user_location_info(request):
    if request.method == 'POST':
        current_user = request.user
        location_json = json.loads(request.body)
        json_data = LocationService(current_user).remove_user_location_info(location_json = location_json)
        context = {'results': json.loads(json_data)}
        return JsonResponse(context)

@basic_auth_required
@csrf_exempt
def update_user_location_info(request):
    if request.method == 'POST':
        current_user = request.user
        location_json = json.loads(request.body)
        json_data = LocationService(current_user).update_user_location_info(location_json = location_json)
        context = {'results': json.loads(json_data)}
        return JsonResponse(context)