import json

from django.http import HttpResponse


def test(request):
    result = {"success":"true"}
    return HttpResponse(json.dumps(result), content_type='application/json')