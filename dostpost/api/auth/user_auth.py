from django.utils.six import wraps
from django.http import HttpResponseForbidden, HttpResponse

from api.handlers.user_model_handler import UserModelHandler

_CURRENT_USER = None

def basic_auth_required(func):
    @wraps(func)
    def _decorator(request, *args, **kwargs):
        if request.META.has_key('HTTP_AUTHORIZATION'):
            authmeth, auth = request.META['HTTP_AUTHORIZATION'].split(' ', 1)
            if authmeth.lower() == 'basic':
                auth = auth.strip().decode('base64')
                username, password = auth.split(':', 1)
                user = UserModelHandler().find_by_emp_id_and_key(username, password)
                if user:
                    request.user = user
                    return func(request, *args, **kwargs)
                else:
                    return HttpResponseForbidden('<h1>Forbidden</h1>')
        res = HttpResponse()
        res.status_code = 401
        res['WWW-Authenticate'] = 'Basic'
        return res
    return _decorator