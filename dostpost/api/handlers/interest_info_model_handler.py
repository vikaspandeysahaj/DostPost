from api.models import InterestInfo


class InterestInfoModelHandler():

    def __init__(self):
        self.model = InterestInfo

    def insert(self,user = None, interest = None, desc = None):
        m = self.model(
            user = user,
            interest = interest,
            desc = desc)
        m.full_clean()
        m.save()
        return m


    def update(self, id, user = None, interest = None, desc = None):
        m = self.find_by_id_and_user(id=id, user=user)
        if m:
            m.interest = interest
            m.desc = desc
            m.full_clean()
            m.save()
        else:
            raise Exception("interest info not found for id %s "%(id))
        return m

    def remove(self, id, user = None):
        m = self.find_by_id_and_user(id=id, user = user)
        if m:
            m.delete()
        else:
            raise Exception("interest info not found for id and user %s, %s"%(id, user.id))
        return m

    def find_all(self):
        m = self.model.objects.all()
        return m

    def find_by_user(self, user):
        m = self.model.objects.filter(user=user)
        return m

    def find_by_id_and_user(self, id, user):
        m = self.model.objects.filter(pk=id, user=user).first()
        return m

    def find_by_id(self, id):
        m = self.model.objects.filter(pk=id).first()
        return m

    def modelname(self):
        return self.model.__name__

