from api.models import PostComment


class PostCommentModelHandler():

    def __init__(self):
        self.model = PostComment

    def insert(self, user = None, post = None, comment = None, media_link = None, post_type = None):
        m = self.model.objects.create()
        m.user = user
        m.post = post
        m.comment = comment
        m.media_link = media_link
        m.post_type = post_type
        m.full_clean()
        m.save()
        return m


    def update(self, id, user = None, post = None, comment = None, media_link = None, post_type = None):
        m = self.find_by_id_and_user(id=id, user=user)
        if m:
            m.post = post
            m.comment = comment
            m.media_link = media_link
            m.post_type = post_type
            m.full_clean()
            m.save()
        else:
            raise Exception("comment  not found for id %s "%(id))
        return m

    def remove(self, id, user = None):
        m = self.find_by_id_and_user(id=id, user = user)
        if m:
            m.delete()
        else:
            raise Exception("comment not found for id and user %s, %s"%(id, user.id))
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

