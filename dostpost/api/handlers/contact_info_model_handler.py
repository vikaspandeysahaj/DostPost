from api.models import ContactInfo


class ContactInfoModelHandler():

    def __init__(self):
        self.model = ContactInfo

    def insert(self, user=None, location = None, email = None, phone = None, mobile = None, address = None):
        m = self.model(
                user =user,
                location = location,
                email = email,
                phone = phone,
                mobile = mobile,
                address = address)
        m.full_clean()
        m.save()
        return m


    def update(self, id, user=None, location = None, email = None, phone = None, mobile = None, address = None):
        m = self.find_by_id_and_user(id=id, user=user)
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

    def find_by_id_and_user(self, id, user):
        m = self.model.objects.filter(pk=id, user=user).first()
        return m

