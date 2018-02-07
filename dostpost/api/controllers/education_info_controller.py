import json

from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

from api.auth.user_auth import basic_auth_required, _CURRENT_USER
from api.services.education_service import EducationService


@basic_auth_required
def get_university_list(request):
    if request.method == 'GET':
        current_user = request.user
        json_data = EducationService(current_user).get_university_list()
        context = {'results': json.loads(json_data)}
        return JsonResponse(context)

@basic_auth_required
def get_user_education_info(request, id):
    if request.method == 'GET':
        current_user = request.user
        json_data = EducationService(current_user).get_user_educations(id)
        context = {'results': json.loads(json_data)}
        return JsonResponse(context)


@basic_auth_required
@csrf_exempt
def add_user_education_info(request):
    if request.method == 'POST':
        current_user = request.user
        education_json = json.loads(request.body)
        json_data = EducationService(current_user).add_user_education_info(education_json = education_json)
        context = {'results': json.loads(json_data)}
        return JsonResponse(context)

@basic_auth_required
@csrf_exempt
def remove_user_education_info(request):
    if request.method == 'POST':
        current_user = request.user
        education_json = json.loads(request.body)
        json_data = EducationService(current_user).remove_user_education_info(education_json = education_json)
        context = {'results': json.loads(json_data)}
        return JsonResponse(context)

@basic_auth_required
@csrf_exempt
def update_user_education_info(request):
    if request.method == 'POST':
        current_user = request.user
        education_json = json.loads(request.body)
        json_data = EducationService(current_user).update_user_education_info(education_json = education_json)
        context = {'results': json.loads(json_data)}
        return JsonResponse(context)