import json

from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

from api.auth.user_auth import basic_auth_required, _CURRENT_USER
from api.services.public_profile_service import PublicProfileService


@basic_auth_required
def get_public_site_list(request):
    if request.method == 'GET':
        current_user = request.user
        json_data = PublicProfileService(current_user).get_public_site_list()
        context = {'results': json.loads(json_data)}
        return JsonResponse(context)

@basic_auth_required
def get_user_public_profile_info(request, id):
    if request.method == 'GET':
        current_user = request.user
        json_data = PublicProfileService(current_user).get_user_public_profiles(id)
        context = {'results': json.loads(json_data)}
        return JsonResponse(context)


@basic_auth_required
@csrf_exempt
def add_user_public_profile_info(request):
    if request.method == 'POST':
        current_user = request.user
        public_profile_json = json.loads(request.body)
        json_data = PublicProfileService(current_user).add_user_public_profile_info(public_profile_json = public_profile_json)
        context = {'results': json.loads(json_data)}
        return JsonResponse(context)

@basic_auth_required
@csrf_exempt
def remove_user_public_profile_info(request):
    if request.method == 'POST':
        current_user = request.user
        public_profile_json = json.loads(request.body)
        json_data = PublicProfileService(current_user).remove_user_public_profile_info(public_profile_json = public_profile_json)
        context = {'results': json.loads(json_data)}
        return JsonResponse(context)

@basic_auth_required
@csrf_exempt
def update_user_public_profile_info(request):
    if request.method == 'POST':
        current_user = request.user
        public_profile_json = json.loads(request.body)
        json_data = PublicProfileService(current_user).update_user_public_profile_info(public_profile_json = public_profile_json)
        context = {'results': json.loads(json_data)}
        return JsonResponse(context)