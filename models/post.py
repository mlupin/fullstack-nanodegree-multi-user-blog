from google.appengine.ext import db
from helpers import *


class Post(db.Model):
    subject = db.StringProperty(required=True)
    content = db.TextProperty(required=True)
    author = db.TextProperty(required=True)
    user_id = db.IntegerProperty(required=True)
    created = db.DateTimeProperty(auto_now_add=True)
    last_modified = db.DateTimeProperty(auto_now=True)

    def render(self, current_user_id):
        key = db.Key.from_path('User', int(self.user_id), parent=users_key())
        user = db.get(key)

        self._render_text = self.content.replace('\n', '<br>')
        return render_str("post.html", post=self,
                          current_user_id=current_user_id,
                          author=user.name)

    @classmethod
    def by_id(cls, uid):
        return Post.get_by_id(uid, parent=blog_key())

    @classmethod
    def get_all(cls):
        return Post.all()

    @classmethod
    def get_ten(cls):
        return Post.all().fetch(limit=10)
