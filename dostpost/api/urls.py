from django.conf.urls import url, include

from api.controllers.login import test

urlpatterns = [
    url(r'^test/$', test, name='test'),
]
