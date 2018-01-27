from api.models import MasterPublicSite


class MasterPublicSiteModelHandler():

    def __init__(self):
        self.model = MasterPublicSite

    def insert(self, site_name = None):
        m = self.find_by_site_name(site_name)
        if not m:
            m = self.model.objects.create()
            m.site_name = site_name
            m.full_clean()
            m.save()
        return m

    def update(self, id, site_name = None):
        m = self.find_by_id(id=id)
        if m:
            m.site_name = site_name
            m.full_clean()
            m.save()
        else:
            raise Exception("site_name not found for id %s "%(id))
        return m

    def find_all(self):
        m = self.model.objects.all()
        return m

    def find_by_site_name(self, site_name):
        m = self.model.objects.filter(site_name=site_name).first()
        return m

    def find_by_id(self, id):
        m = self.model.objects.filter(pk=id).first()
        return m

    def modelname(self):
        return self.model.__name__

