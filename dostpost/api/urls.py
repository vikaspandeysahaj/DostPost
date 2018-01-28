from django.conf.urls import url, include

from api.controllers.login import test
from api.controllers.project_info_controller import get_project_list, get_user_project, add_user_project, \
    remove_user_project
from api.controllers.user_controller import get_user_list, get_user_profile

urlpatterns = [
    url(r'^test/$', test, name='test'),

    # core api for users
    url(r'^user/list', get_user_list, name='user_list'),
    url(r'^user/([0-9]+)$', get_user_profile, name='user_profile'),

    # Project related apis
    url(r'^projects/', get_project_list, name='master_project_list'),
    url(r'^user/([0-9]+)/projects/$', get_user_project, name='project_info_list'),
    url(r'^user/project/add/$', add_user_project, name='add_project_info'),
    url(r'^user/project/remove/$', remove_user_project, name='remove_project_info'),




]
