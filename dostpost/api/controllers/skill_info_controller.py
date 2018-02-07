import json

from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

from api.auth.user_auth import basic_auth_required, _CURRENT_USER
from api.services.skill_service import SkillService


@basic_auth_required
def get_skill_list(request):
    if request.method == 'GET':
        current_user = request.user
        json_data = SkillService(current_user).get_skill_list()
        context = {'results': json.loads(json_data)}
        return JsonResponse(context)

@basic_auth_required
def get_user_skill_info(request, id):
    if request.method == 'GET':
        current_user = request.user
        json_data = SkillService(current_user).get_user_skills(id)
        context = {'results': json.loads(json_data)}
        return JsonResponse(context)


@basic_auth_required
@csrf_exempt
def add_user_skill_info(request):
    if request.method == 'POST':
        current_user = request.user
        skill_json = json.loads(request.body)
        json_data = SkillService(current_user).add_user_skill_info(skill_json = skill_json)
        context = {'results': json.loads(json_data)}
        return JsonResponse(context)

@basic_auth_required
@csrf_exempt
def remove_user_skill_info(request):
    if request.method == 'POST':
        current_user = request.user
        skill_json = json.loads(request.body)
        json_data = SkillService(current_user).remove_user_skill_info(skill_json = skill_json)
        context = {'results': json.loads(json_data)}
        return JsonResponse(context)

@basic_auth_required
@csrf_exempt
def update_user_skill_info(request):
    if request.method == 'POST':
        current_user = request.user
        skill_json = json.loads(request.body)
        json_data = SkillService(current_user).update_user_skill_info(skill_json = skill_json)
        context = {'results': json.loads(json_data)}
        return JsonResponse(context)