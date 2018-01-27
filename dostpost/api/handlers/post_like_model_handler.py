from api.models import PostLike


class PostLikeModelHandler():

    def __init__(self):
        self.model = PostLike

    def insert(self, user = None, post = None):
        m = self.model.objects.create()
        m.user = user
        m.post = post
        m.full_clean()
        m.save()
        return m

    def remove(self, id, user = None, post = None):
        m = self.find_by_id_and_user_and_post(id=id, user = user, post=post)
        if m:
            m.delete()
        else:
            raise Exception("like not found for id and user %s, %s"%(id, user.id))
        return m

    def find_all(self):
        m = self.model.objects.all()
        return m

    def find_by_user(self, user):
        m = self.model.objects.filter(user=user).first()
        return m

    def find_by_id_and_user_and_post(self, id, user, post):
        m = self.model.objects.filter(pk=id, user=user, post=post).first()
        return m

    def find_by_id(self, id):
        m = self.model.objects.filter(pk=id).first()
        return m

    def modelname(self):
        return self.model.__name__

