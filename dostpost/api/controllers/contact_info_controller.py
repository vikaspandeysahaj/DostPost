import json

from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

from api.auth.user_auth import basic_auth_required, _CURRENT_USER
from api.services.contact_service import ContactService



@basic_auth_required
def get_user_contact_info(request, id):
    if request.method == 'GET':
        current_user = request.user
        json_data = ContactService(current_user).get_user_contact_info(id)
        context = {'results': json.loads(json_data)}
        return JsonResponse(context)


@basic_auth_required
@csrf_exempt
def add_user_contact_info(request):
    if request.method == 'POST':
        current_user = request.user
        contact_json = json.loads(request.body)
        json_data = ContactService(current_user).add_user_contact_info(contact_json = contact_json)
        context = {'results': json.loads(json_data)}
        return JsonResponse(context)

@basic_auth_required
@csrf_exempt
def update_user_contact_info(request):
    if request.method == 'POST':
        current_user = request.user
        contact_json = json.loads(request.body)
        json_data = ContactService(current_user).update_user_contact_info(contact_json = contact_json)
        context = {'results': json.loads(json_data)}
        return JsonResponse(context)