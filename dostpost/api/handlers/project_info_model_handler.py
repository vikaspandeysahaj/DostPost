from api.models import ProjectInfo


class ProjectInfoModelHandler():

    def __init__(self):
        self.model = ProjectInfo

    def insert(self, user = None, project = None, location = None, start_date = None, end_date = None):

        m = self.model.objects.create()
        m.user = user
        m.project = project
        m.location = location
        m.start_date = start_date
        m.end_date = end_date
        m.full_clean()
        m.save()
        return m

    def update(self, id, user = None, project = None, location = None, start_date = None, end_date = None):
        m = self.find_by_id_and_user(id=id, user=user)
        if m:
            m.project = project
            m.location = location
            m.start_date = start_date
            m.end_date = end_date
            m.full_clean()
            m.save()
        else:
            raise Exception("project info not found for id %s "%(id))
        return m

    def remove(self, id, user = None):
        m = self.find_by_id_and_user(id=id, user = user)
        if m:
            m.delete()
        else:
            raise Exception("project info not found for id and user %s, %s"%(id, user.id))
        return m

    def find_all(self):
        m = self.model.objects.all()
        return m

    def find_by_user(self, user):
        m = self.model.objects.filter(user=user).first()
        return m

    def find_by_id_and_user(self, id, user):
        m = self.model.objects.filter(pk=id, user=user).first()
        return m

    def find_by_id(self, id):
        m = self.model.objects.filter(pk=id).first()
        return m

    def modelname(self):
        return self.model.__name__

