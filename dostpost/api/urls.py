from django.conf.urls import url, include

from api.controllers.contact_info_controller import get_user_contact_info, add_user_contact_info, update_user_contact_info
from api.controllers.education_info_controller import get_university_list, get_user_education_info, \
    add_user_education_info, remove_user_education_info, update_user_education_info
from api.controllers.interest_info_controller import get_interest_list, get_user_interest_info, add_user_interest_info, \
    remove_user_interest_info, update_user_interest_info
from api.controllers.location_info_controller import get_location_list, get_user_location_info, add_user_location_info, \
    remove_user_location_info, update_user_location_info
from api.controllers.login import test
from api.controllers.project_info_controller import get_project_list, get_user_project, add_user_project, \
    remove_user_project, update_user_project
from api.controllers.public_profile_info_controller import get_public_site_list, get_user_public_profile_info, \
    add_user_public_profile_info, remove_user_public_profile_info, update_user_public_profile_info
from api.controllers.salary_info_controller import get_user_salary_info, add_user_salary_info, update_user_salary_info
from api.controllers.skill_info_controller import get_skill_list, get_user_skill_info, add_user_skill_info, \
    remove_user_skill_info, update_user_skill_info
from api.controllers.user_controller import get_user_list, get_user_profile
from api.controllers.work_info_controller import get_company_list, get_user_work_info, add_user_work_info, \
    remove_user_work_info, update_user_work_info, get_designation_list

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
    url(r'^user/project/update/$', update_user_project, name='update_project_info'),

    # Contact related apis
    url(r'^user/([0-9]+)/contacts/$', get_user_contact_info, name='contact_info_list'),
    url(r'^user/contact/add/$', add_user_contact_info, name='add_contact_info'),
    url(r'^user/contact/update/$', update_user_contact_info, name='update_contact_info'),

    # Education related apis
    url(r'^universities/', get_university_list, name='master_university_list'),
    url(r'^user/([0-9]+)/educations/$', get_user_education_info, name='get_user_education_info'),
    url(r'^user/education/add/$', add_user_education_info, name='add_user_education_info'),
    url(r'^user/education/remove/$', remove_user_education_info, name='remove_user_education_info'),
    url(r'^user/education/update/$', update_user_education_info, name='update_user_education_info'),

    # Location related apis
    url(r'^locations/', get_location_list, name='master_location_list'),
    url(r'^user/([0-9]+)/locations/$', get_user_location_info, name='get_user_location_info'),
    url(r'^user/location/add/$', add_user_location_info, name='add_user_location_info'),
    url(r'^user/location/remove/$', remove_user_location_info, name='remove_user_location_info'),
    url(r'^user/location/update/$', update_user_location_info, name='update_user_location_info'),

    # Interest related apis
    url(r'^interests/', get_interest_list, name='master_interest_list'),
    url(r'^user/([0-9]+)/interests/$', get_user_interest_info, name='get_user_interest_info'),
    url(r'^user/interest/add/$', add_user_interest_info, name='add_user_interest_info'),
    url(r'^user/interest/remove/$', remove_user_interest_info, name='remove_user_interest_info'),
    url(r'^user/interest/update/$', update_user_interest_info, name='update_user_interest_info'),

    # Salary related apis
    url(r'^user/([0-9]+)/salary/$', get_user_salary_info, name='get_user_salary_info'),
    url(r'^user/salary/add/$', add_user_salary_info, name='add_user_salary_info'),
    url(r'^user/salary/update/$', update_user_salary_info, name='update_user_salary_info'),

    # Skill related apis
    url(r'^skills/', get_skill_list, name='master_skill_list'),
    url(r'^user/([0-9]+)/skills/$', get_user_skill_info, name='get_user_skill_info'),
    url(r'^user/skill/add/$', add_user_skill_info, name='add_user_skill_info'),
    url(r'^user/skill/remove/$', remove_user_skill_info, name='remove_user_skill_info'),
    url(r'^user/skill/update/$', update_user_skill_info, name='update_user_skill_info'),

    # Work related apis
    url(r'^companies/', get_company_list, name='master_company_list'),
    url(r'^designations/', get_designation_list, name='master_designation_list'),
    url(r'^user/([0-9]+)/works/$', get_user_work_info, name='get_user_work_info'),
    url(r'^user/work/add/$', add_user_work_info, name='add_user_work_info'),
    url(r'^user/work/remove/$', remove_user_work_info, name='remove_user_work_info'),
    url(r'^user/work/update/$', update_user_work_info, name='update_user_work_info'),

    # Public Profile related apis
    url(r'^public_sites/', get_public_site_list, name='master_skill_list'),
    url(r'^user/([0-9]+)/public_profiles/$', get_user_public_profile_info, name='get_user_public_profile_info'),
    url(r'^user/public_profile/add/$', add_user_public_profile_info, name='add_user_public_profile_info'),
    url(r'^user/public_profile/remove/$', remove_user_public_profile_info, name='remove_user_public_profile_info'),
    url(r'^user/public_profile/update/$', update_user_public_profile_info, name='update_user_public_profile_info'),
]
