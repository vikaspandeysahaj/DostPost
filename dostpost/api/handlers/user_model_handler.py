from api.models import User

class UserModelHandler():

    def __init__(self):
        self.model = User

    def insert(self, employee_id = None, full_name=None, first_name = None, middle_name = None, last_name = None, Gender = None, DOB = None, marital_status = None):
        m = self.model(
            employee_id = employee_id,
            full_name = full_name,
            first_name = first_name,
            middle_name = middle_name,
            last_name = last_name,
            Gender = Gender,
            DOB = DOB,
            marital_status = marital_status)
        m.full_clean()
        m.save()
        return m

    def update(self, id, full_name=None, first_name = None, middle_name = None, last_name = None, Gender = None, DOB = None, marital_status = None):
        m = self.find_by_id(id=id)
        if m:
            m.full_name = full_name
            m.first_name = first_name
            m.middle_name = middle_name
            m.last_name = last_name
            m.Gender = Gender
            m.DOB = DOB
            m.marital_status = marital_status
            m.full_clean()
            m.save()
        else:
            raise Exception("User not found for id %s "%(id))
        return m

    def find_all(self):
        m = self.model.objects.all()
        return m

    def find_by_id(self, id):
        m = self.model.objects.filter(pk=id).first()
        return m

    def modelname(self):
        return self.model.__name__

