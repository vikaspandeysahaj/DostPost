import json

from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

from api.auth.user_auth import basic_auth_required, _CURRENT_USER
from api.services.work_service import WorkService


@basic_auth_required
def get_company_list(request):
    if request.method == 'GET':
        current_user = request.user
        json_data = WorkService(current_user).get_company_list()
        context = {'results': json.loads(json_data)}
        return JsonResponse(context)


@basic_auth_required
def get_designation_list(request):
    if request.method == 'GET':
        current_user = request.user
        json_data = WorkService(current_user).get_designation_list()
        context = {'results': json.loads(json_data)}
        return JsonResponse(context)

@basic_auth_required
def get_user_work_info(request, id):
    if request.method == 'GET':
        current_user = request.user
        json_data = WorkService(current_user).get_user_works(id)
        context = {'results': json.loads(json_data)}
        return JsonResponse(context)


@basic_auth_required
@csrf_exempt
def add_user_work_info(request):
    if request.method == 'POST':
        current_user = request.user
        work_json = json.loads(request.body)
        json_data = WorkService(current_user).add_user_work_info(work_json = work_json)
        context = {'results': json.loads(json_data)}
        return JsonResponse(context)

@basic_auth_required
@csrf_exempt
def remove_user_work_info(request):
    if request.method == 'POST':
        current_user = request.user
        work_json = json.loads(request.body)
        json_data = WorkService(current_user).remove_user_work_info(work_json = work_json)
        context = {'results': json.loads(json_data)}
        return JsonResponse(context)

@basic_auth_required
@csrf_exempt
def update_user_work_info(request):
    if request.method == 'POST':
        current_user = request.user
        work_json = json.loads(request.body)
        json_data = WorkService(current_user).update_user_work_info(work_json = work_json)
        context = {'results': json.loads(json_data)}
        return JsonResponse(context)