import json

from rest_framework.renderers import JSONRenderer


from api.handlers.salary_info_model_handler import SalaryInfoModelHandler
from api.handlers.user_model_handler import UserModelHandler
from api.serializers.salary_info_serializers import SalaryInfoSerializer


class SalaryService():

    def __init__(self, current_user):
        self.current_user = current_user


    def get_user_salarys(self, user_id):
        try:
            for_user = UserModelHandler().find_by_id(user_id)
            if for_user:
                queryset = SalaryInfoModelHandler().find_by_user(for_user)
                data = SalaryInfoSerializer(queryset).data
                json_data = JSONRenderer().render(data)
                return json_data
            else:
                return json.dumps({"Error":"User Not found"})
        except Exception as ex:
            return json.dumps({"Error":"Not able to fetch the salarys : %s"%(ex.message)})

    def add_user_salary_info(self, salary_json):
        try:

            created_salary_info = SalaryInfoModelHandler().insert(
                user = self.current_user,
                salary = salary_json["salary"],
                revised_date = salary_json["revised_date"])

            data = SalaryInfoSerializer(created_salary_info).data
            json_data = JSONRenderer().render(data)
            return json_data
        except Exception as ex:
            return json.dumps({"Error":"Not able to add the salary : %s"%(ex.message)})

    def remove_user_salary_info(self, salary_json):
        try:
            salary_id = salary_json["id"]
            deleted_salary = SalaryInfoModelHandler().remove(salary_id, self.current_user)
            return json.dumps({"Sucess":"Salary removed %s"%(deleted_salary.id)})
        except Exception as ex:
            return json.dumps({"Error":"Not able to remove the salary : %s"%(ex.message)})

    def update_user_salary_info(self, salary_json):
        try:

            updated_salary_info = SalaryInfoModelHandler().update(
                id = salary_json["id"],
                user = self.current_user,
                salary = salary_json["salary"],
                revised_date = salary_json["revised_date"])

            data = SalaryInfoSerializer(updated_salary_info).data
            json_data = JSONRenderer().render(data)
            return json_data
        except Exception as ex:
            return json.dumps({"Error":"Not able to update the salary : %s"%(ex.message)})


