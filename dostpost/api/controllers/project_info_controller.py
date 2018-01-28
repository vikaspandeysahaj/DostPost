import json

from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

from api.auth.user_auth import basic_auth_required, _CURRENT_USER
from api.services.project_service import ProjectService


@basic_auth_required
def get_project_list(request):
    if request.method == 'GET':
        current_user = request.user
        json_data = ProjectService(current_user).get_project_list()
        context = {'results': json.loads(json_data)}
        return JsonResponse(context)

@basic_auth_required
def get_user_project(request, id):
    if request.method == 'GET':
        current_user = request.user
        json_data = ProjectService(current_user).get_user_projects(id)
        context = {'results': json.loads(json_data)}
        return JsonResponse(context)


@basic_auth_required
@csrf_exempt
def add_user_project(request):
    if request.method == 'POST':
        current_user = request.user
        project_json = json.loads(request.body)
        json_data = ProjectService(current_user).add_user_project_info(project_json = project_json)
        context = {'results': json.loads(json_data)}
        return JsonResponse(context)

@basic_auth_required
@csrf_exempt
def remove_user_project(request):
    if request.method == 'POST':
        current_user = request.user
        project_json = json.loads(request.body)
        json_data = ProjectService(current_user).remove_user_project_info(project_json = project_json)
        context = {'results': json.loads(json_data)}
        return JsonResponse(context)