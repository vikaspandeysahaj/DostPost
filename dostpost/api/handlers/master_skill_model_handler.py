from api.models import MasterSkill


class MasterSkillModelHandler():

    def __init__(self):
        self.model = MasterSkill

    def insert(self, skill_name = None):
        m = self.find_by_skill_name(skill_name)
        if not m:
            m = self.model.objects.create()
            m.skill_name = skill_name
            m.full_clean()
            m.save()
        return m

    def update(self, id, skill_name = None):
        m = self.find_by_id(id=id)
        if m:
            m.skill_name = skill_name
            m.full_clean()
            m.save()
        else:
            raise Exception("skill_name not found for id %s "%(id))
        return m

    def find_all(self):
        m = self.model.objects.all()
        return m

    def find_by_skill_name(self, skill_name):
        m = self.model.objects.filter(skill_name=skill_name).first()
        return m

    def find_by_id(self, id):
        m = self.model.objects.filter(pk=id).first()
        return m

    def modelname(self):
        return self.model.__name__

