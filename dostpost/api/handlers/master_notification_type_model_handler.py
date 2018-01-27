from api.models import MasterNotificationType


class MasterNotificationTypeModelHandler():

    def __init__(self):
        self.model = MasterNotificationType

    def insert(self, notification_name = None):
        m = self.find_by_notification_name(notification_name)
        if not m:
            m = self.model.objects.create()
            m.notification_name = notification_name
            m.full_clean()
            m.save()
        return m

    def update(self, id, notification_name = None):
        m = self.find_by_id(id=id)
        if m:
            m.notification_name = notification_name
            m.full_clean()
            m.save()
        else:
            raise Exception("notification_name not found for id %s "%(id))
        return m

    def find_all(self):
        m = self.model.objects.all()
        return m

    def find_by_notification_name(self, notification_name):
        m = self.model.objects.filter(notification_name=notification_name).first()
        return m

    def find_by_id(self, id):
        m = self.model.objects.filter(pk=id).first()
        return m

    def modelname(self):
        return self.model.__name__

