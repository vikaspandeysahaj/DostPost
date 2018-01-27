from api.models import MasterMaritalStatus


class MasterMaritalStatusModelHandler():

    def __init__(self):
        self.model = MasterMaritalStatus

    def insert(self, marital_status = None):
        m = self.find_by_status(marital_status)
        if not m:
            m = self.model.objects.create()
            m.status = marital_status
            m.full_clean()
            m.save()
        return m

    def update(self, id, marital_status = None):
        m = self.find_by_id(id=id)
        if m:
            m.status = marital_status
            m.full_clean()
            m.save()
        else:
            raise Exception("marital status not found for id %s "%(id))
        return m

    def delete(self):
        pass

    def find_all(self):
        m = self.model.objects.all()
        return m

    def find_by_status(self, marital_status):
        m = self.model.objects.filter(status=marital_status).first()
        return m

    def find_by_id(self, id):
        m = self.model.objects.filter(pk=id).first()
        return m

    def modelname(self):
        return self.model.__name__

