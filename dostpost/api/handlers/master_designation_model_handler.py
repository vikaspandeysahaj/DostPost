from api.models import MasterDesignation


class MasterDesignationModelHandler():

    def __init__(self):
        self.model = MasterDesignation

    def insert(self, designation_name = None):
        m = self.find_by_designation_name(designation_name)
        if not m:
            m = self.model.objects.create()
            m.designation_name = designation_name
            m.full_clean()
            m.save()
        return m

    def update(self, id, designation_name = None):
        m = self.find_by_id(id=id)
        if m:
            m.designation_name = designation_name
            m.full_clean()
            m.save()
        else:
            raise Exception("designation_name not found for id %s "%(id))
        return m

    def find_all(self):
        m = self.model.objects.all()
        return m

    def find_by_designation_name(self, designation_name):
        m = self.model.objects.filter(designation_name=designation_name).first()
        return m

    def find_by_id(self, id):
        m = self.model.objects.filter(pk=id).first()
        return m

    def modelname(self):
        return self.model.__name__

