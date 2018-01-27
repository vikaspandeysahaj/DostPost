from api.models import SkillInfo


class SkillInfoModelHandler():

    def __init__(self):
        self.model = SkillInfo

    def insert(self, user = None, skill = None, rank = None):

        m = self.model.objects.create()
        m.user = user
        m.skill = skill
        m.rank = rank
        m.full_clean()
        m.save()
        return m

    def update(self, id,  user = None, skill = None, rank = None):
        m = self.find_by_id_and_user(id=id, user=user)
        if m:
            m.skill = skill
            m.rank = rank
            m.full_clean()
            m.save()
        else:
            raise Exception(" Skill info not found for id %s "%(id))
        return m

    def remove(self, id, user = None):
        m = self.find_by_id_and_user(id=id, user = user)
        if m:
            m.delete()
        else:
            raise Exception("Skill  info not found for id and user %s, %s"%(id, user.id))
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

