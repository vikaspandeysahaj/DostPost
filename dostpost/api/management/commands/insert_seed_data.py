from django.core.management.base import BaseCommand

from api.handlers.master_marital_status_model_handler import MasterMaritalStatusModelHandler
from api.handlers.user_model_handler import UserModelHandler


class Command(BaseCommand):
    help = 'Insert seed data in tables'

    def add_arguments(self, parser):
        # parser.add_argument('poll_id', nargs='+', type=int)
        pass

    def handle(self, *args, **options):
        marital_model_handler = MasterMaritalStatusModelHandler()
        user_model_handler = UserModelHandler()

        try:
            self.stdout.write(self.style.SUCCESS('Inserting seed value into marital_status ...'))
            marital_model_handler.insert(marital_status="Single")
            marital_model_handler.insert(marital_status="In Relationship")
            marital_model_handler.insert(marital_status="Married")
            self.stdout.write(self.style.SUCCESS('Successfully inserted into marital_status.'))


            self.stdout.write(self.style.SUCCESS('Inserting seed value into User ...'))
            married = marital_model_handler.find_by_status("Married")
            single = marital_model_handler.find_by_status("Single")

            user_model_handler.insert(employee_id = "1004", full_name="Vikas Pandey", first_name="Vikas", last_name="Pandey", Gender="Male", DOB="06-08-1986", marital_status=married)
            user_model_handler.insert(employee_id = "1005",full_name="Vijay Kumar", first_name="Vijay", last_name="Kumar", Gender="Male", DOB="31-03-1986", marital_status=married)
            user_model_handler.insert(employee_id = "1006", full_name="Riyas P", first_name="Riyas", last_name="P", Gender="Male", DOB="01-12-1999", marital_status=single)

            self.stdout.write(self.style.SUCCESS('Successfully inserted into User.'))

        except Exception as e:
            raise e



