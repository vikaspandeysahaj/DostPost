from api.models import ContactInfo


class ContactInfoModelHandler():

    def __init__(self):
        self.model = ContactInfo

    def insert(self, user=None, location = None, email = None, phone = None, mobile = None, address = None):
        m = self.model.objects.create()
        m.user =user
        m.location = location
        m.email = email
        m.phone = phone
        m.mobile = mobile
        m.address = address
        m.full_clean()
        m.save()
        return m


    def update(self, id, user=None, location = None, email = None, phone = None, mobile = None, address = None):
        m = self.find_by_id(id=id)
        if m:
            m.location = location
            m.email = email
            m.phone = phone
            m.mobile = mobile
            m.address = address
            m.full_clean()
            m.save()
        else:
            raise Exception("contact info not found for id %s "%(id))
        return m

    def find_all(self):
        m = self.model.objects.all()
        return m

    def find_by_user(self, user):
        m = self.model.objects.filter(user=user).first()
        return m

    def find_by_id(self, id):
        m = self.model.objects.filter(pk=id).first()
        return m

    def modelname(self):
        return self.model.__name__

