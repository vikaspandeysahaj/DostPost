from django.conf.urls import url, include

from api.controllers.login import test
from api.controllers.user_controller import get_user_list, get_user_profile

urlpatterns = [
    url(r'^test/$', test, name='test'),
    url(r'^user/list', get_user_list, name='user_list'),
    url(r'^user/([0-9]+)$', get_user_profile, name='user_profile'),

]
