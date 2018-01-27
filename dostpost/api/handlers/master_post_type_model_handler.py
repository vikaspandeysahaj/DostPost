from api.models import MasterPostType


class MasterPostTypeModelHandler():

    def __init__(self):
        self.model = MasterPostType

    def insert(self, post_type = None):
        m = self.find_by_post_type(post_type)
        if not m:
            m = self.model.objects.create()
            m.post_type = post_type
            m.full_clean()
            m.save()
        return m

    def update(self, id, post_type = None):
        m = self.find_by_id(id=id)
        if m:
            m.post_type = post_type
            m.full_clean()
            m.save()
        else:
            raise Exception("post_type not found for id %s "%(id))
        return m

    def find_all(self):
        m = self.model.objects.all()
        return m

    def find_by_post_type(self, post_type):
        m = self.model.objects.filter(post_type=post_type).first()
        return m

    def find_by_id(self, id):
        m = self.model.objects.filter(pk=id).first()
        return m

    def modelname(self):
        return self.model.__name__

