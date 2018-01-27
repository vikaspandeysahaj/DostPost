from api.models import MasterEducationType


class MasterEducationTypeModelHandler():

    def __init__(self):
        self.model = MasterEducationType

    def insert(self, education_type = None):
        m = self.find_by_education_type(education_type)
        if not m:
            m = self.model.objects.create()
            m.education_type = education_type
            m.full_clean()
            m.save()
        return m

    def update(self, id, education_type = None):
        m = self.find_by_id(id=id)
        if m:
            m.education_type = education_type
            m.full_clean()
            m.save()
        else:
            raise Exception("education_type not found for id %s "%(id))
        return m

    def find_all(self):
        m = self.model.objects.all()
        return m

    def find_by_education_type(self, education_type):
        m = self.model.objects.filter(education_type=education_type).first()
        return m

    def find_by_id(self, id):
        m = self.model.objects.filter(pk=id).first()
        return m

    def modelname(self):
        return self.model.__name__

