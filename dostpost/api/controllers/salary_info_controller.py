import json

from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

from api.auth.user_auth import basic_auth_required, _CURRENT_USER
from api.services.salary_service import SalaryService



@basic_auth_required
def get_user_salary_info(request, id):
    if request.method == 'GET':
        current_user = request.user
        json_data = SalaryService(current_user).get_user_salarys(id)
        context = {'results': json.loads(json_data)}
        return JsonResponse(context)


@basic_auth_required
@csrf_exempt
def add_user_salary_info(request):
    if request.method == 'POST':
        current_user = request.user
        salary_json = json.loads(request.body)
        json_data = SalaryService(current_user).add_user_salary_info(salary_json = salary_json)
        context = {'results': json.loads(json_data)}
        return JsonResponse(context)

@basic_auth_required
@csrf_exempt
def remove_user_salary_info(request):
    if request.method == 'POST':
        current_user = request.user
        salary_json = json.loads(request.body)
        json_data = SalaryService(current_user).remove_user_salary_info(salary_json = salary_json)
        context = {'results': json.loads(json_data)}
        return JsonResponse(context)

@basic_auth_required
@csrf_exempt
def update_user_salary_info(request):
    if request.method == 'POST':
        current_user = request.user
        salary_json = json.loads(request.body)
        json_data = SalaryService(current_user).update_user_salary_info(salary_json = salary_json)
        context = {'results': json.loads(json_data)}
        return JsonResponse(context)