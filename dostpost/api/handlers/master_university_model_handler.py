from api.models import MasterUniversity


class MasterUniversityModelHandler():

    def __init__(self):
        self.model = MasterUniversity

    def insert(self, university_name = None):
        m = self.find_by_university_name(university_name)
        if not m:
            m = self.model.objects.create()
            m.university_name = university_name
            m.full_clean()
            m.save()
        return m

    def update(self, id, university_name = None):
        m = self.find_by_id(id=id)
        if m:
            m.university_name = university_name
            m.full_clean()
            m.save()
        else:
            raise Exception("university_name not found for id %s "%(id))
        return m

    def find_all(self):
        m = self.model.objects.all()
        return m

    def find_by_university_name(self, university_name):
        m = self.model.objects.filter(university_name=university_name).first()
        return m

    def find_by_id(self, id):
        m = self.model.objects.filter(pk=id).first()
        return m

    def modelname(self):
        return self.model.__name__

