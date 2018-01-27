from api.models import MasterCompany


class MasterCompanyModelHandler():

    def __init__(self):
        self.model = MasterCompany

    def insert(self, company_name = None):
        m = self.find_by_company_name(company_name)
        if not m:
            m = self.model.objects.create()
            m.company_name = company_name
            m.full_clean()
            m.save()
        return m

    def update(self, id, company_name = None):
        m = self.find_by_id(id=id)
        if m:
            m.company_name = company_name
            m.full_clean()
            m.save()
        else:
            raise Exception("company_name not found for id %s "%(id))
        return m

    def find_all(self):
        m = self.model.objects.all()
        return m

    def find_by_company_name(self, company_name):
        m = self.model.objects.filter(company_name=company_name).first()
        return m

    def find_by_id(self, id):
        m = self.model.objects.filter(pk=id).first()
        return m

    def modelname(self):
        return self.model.__name__

