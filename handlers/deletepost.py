from handlers.blog import BlogHandler
from google.appengine.ext import db
from helpers import *
import time


class DeletePost(BlogHandler):
    def get(self, post_id):
        # Logged in users can delete posts
        if self.user:
            key = db.Key.from_path('Post', int(post_id), parent=blog_key())
            post = db.get(key)

            # Users can only delete posts they themselves have made
            if post and post.user_id == self.user.key().id():
                self.render('deletepost.html', post=post)
            else:
                self.redirect('/blog')
        # Logged out users are redirected to the login page
        else:
            self.redirect('/signin')

    def post(self, post_id):
        key = db.Key.from_path('Post', int(post_id), parent=blog_key())
        post = db.get(key)
        post.delete()
        time.sleep(0.1)
        self.redirect('/blog')
