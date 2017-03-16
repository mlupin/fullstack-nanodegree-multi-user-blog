from handlers.blog import BlogHandler
from google.appengine.ext import db
from helpers import *
from models.comment import Comment
import time


class EditComment(BlogHandler):
    def get(self, post_id):
        if self.user:
            key = db.Key.from_path('Post', int(post_id), parent=blog_key())
            post = db.get(key)
            if post and post.user_id == self.user.key().id():
                self.render('deletepost.html', post=post)
            else:
                self.redirect('/blog')
        else:
            self.redirect('/signin')

    def post(self, post_id):
        key = db.Key.from_path('Post', int(post_id), parent=blog_key())
        post = db.get(key)
        post.delete()
        time.sleep(0.1)
        self.redirect('/blog')
