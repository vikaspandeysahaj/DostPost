from api.models import MasterInterest


class MasterInterestModelHandler():

    def __init__(self):
        self.model = MasterInterest

    def insert(self, interest_name = None):
        m = self.find_by_interest_name(interest_name)
        if not m:
            m = self.model.objects.create()
            m.interest_name = interest_name
            m.full_clean()
            m.save()
        return m

    def update(self, id, interest_name = None):
        m = self.find_by_id(id=id)
        if m:
            m.interest_name = interest_name
            m.full_clean()
            m.save()
        else:
            raise Exception("interest_name not found for id %s "%(id))
        return m

    def find_all(self):
        m = self.model.objects.all()
        return m

    def find_by_interest_name(self, interest_name):
        m = self.model.objects.filter(interest_name=interest_name).first()
        return m

    def find_by_id(self, id):
        m = self.model.objects.filter(pk=id).first()
        return m

    def modelname(self):
        return self.model.__name__

