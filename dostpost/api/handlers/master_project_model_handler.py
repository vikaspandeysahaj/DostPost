from api.models import MasterProject


class MasterProjectModelHandler():

    def __init__(self):
        self.model = MasterProject

    def insert(self, project_name = None):
        m = self.find_by_project_name(project_name)
        if not m:
            m = self.model.objects.create()
            m.project_name = project_name
            m.full_clean()
            m.save()
        return m

    def update(self, id, project_name = None):
        m = self.find_by_id(id=id)
        if m:
            m.project_name = project_name
            m.full_clean()
            m.save()
        else:
            raise Exception("project_name not found for id %s "%(id))
        return m

    def find_all(self):
        m = self.model.objects.all()
        return m

    def find_by_project_name(self, project_name):
        m = self.model.objects.filter(project_name=project_name).first()
        return m

    def find_by_id(self, id):
        m = self.model.objects.filter(pk=id).first()
        return m

    def modelname(self):
        return self.model.__name__

