from handlers.blog import BlogHandler
from google.appengine.ext import db
from helpers import *
import time


class DeletePost(BlogHandler):
    @signin_required
    def get(self, post_id):
        # Logged in users can delete posts
        key = db.Key.from_path('Post', int(post_id), parent=blog_key())
        post = db.get(key)

        # Users can only delete posts they themselves have made
        if post is not None and self.user.key().id() == int(post.user_id):
            return self.render('deletepost.html', post=post)
        else:
            return self.redirect('/blog')

    @signin_required
    def post(self, post_id):
        key = db.Key.from_path('Post', int(post_id), parent=blog_key())
        post = db.get(key)

        # Users can only delete posts they themselves have made
        if post is not None and self.user.key().id() == int(post.user_id):
            key = db.Key.from_path('Post', int(post_id), parent=blog_key())
            post = db.get(key)
            post.delete()
            time.sleep(0.1)
            return self.redirect('/blog')
        else:
            return self.redirect('/blog')
