from api.models import MasterLocation


class MasterLocationModelHandler():

    def __init__(self):
        self.model = MasterLocation

    def insert(self, location_name = None):
        m = self.find_by_location_name(location_name)
        if not m:
            m = self.model.objects.create()
            m.location_name = location_name
            m.full_clean()
            m.save()
        return m

    def update(self, id, location_name = None):
        m = self.find_by_id(id=id)
        if m:
            m.location_name = location_name
            m.full_clean()
            m.save()
        else:
            raise Exception("location_name not found for id %s "%(id))
        return m

    def find_all(self):
        m = self.model.objects.all()
        return m

    def find_by_location_name(self, location_name):
        m = self.model.objects.filter(location_name=location_name).first()
        return m

    def find_by_id(self, id):
        m = self.model.objects.filter(pk=id).first()
        return m

    def modelname(self):
        return self.model.__name__

