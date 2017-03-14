from google.appengine.ext import db
from helpers import *


class Post(db.Model):
    subject = db.StringProperty(required=True)
    content = db.TextProperty(required=True)
    post_id = db.StringProperty(required=True)
    author = db.StringProperty(required=True)
    created = db.DateTimeProperty(auto_now_add=True)
    last_modified = db.DateTimeProperty(auto_now=True)

    @classmethod
    def get_all(cls):
        return Post.all()

    @classmethod
    def get_ten(cls):
        return Post.all().fetch(limit=10)

    def render(self, current_user_id):
        key = db.Key.from_path('User', int(self.user_id), parent=users_key())
        user = db.get(key)

        self._render_text = self.content.replace('\n', '<br>')
        return render_str("post.html", p=self, current_user_id=current_user_id, author=user.name)

    @classmethod
    def create(cls, post_id, subject, content, author):
        return Post(post_id=post_id,
                    subject=subject,
                    content=content,
                    author=author
                    )

    @classmethod
    def edit(cls, post_id, subject, content, username):
        post = Post.by_post_id(post_id)
        if post and username == post.author:
                post.subject = subject
                post.content = content
                post.put()
                return True
        return False

    @classmethod
    def delete(cls, post_id, username):
        post = Post.by_post_id(post_id)
        if post and username == post.author:
                db.delete(post)
                return True
        return False
