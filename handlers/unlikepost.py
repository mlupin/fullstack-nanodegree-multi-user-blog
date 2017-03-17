from handlers.blog import BlogHandler
from google.appengine.ext import db
from models.like import Like
from helpers import *
import time


class UnlikePost(BlogHandler):
    def get(self, post_id):
        key = db.Key.from_path('Post', int(post_id), parent=blog_key())
        post = db.get(key)

        # Logged in users can unlike a post if a post exists
        if self.user and post:
            user_id = self.user.key().id()
            post_id = post.key().id()

            like = Like.all().filter('user_id =', user_id).filter('post_id =', post_id).get()

            # Logged in users can only unlike posts if their have liked it before
            if like and like.user_id == self.user.key().id():
                # Cannot dislike a post if it has 0 likes
                # Decrease likes count by 1
                like.delete()
                post.likes -= 1
                post.put()
                time.sleep(0.1)
                self.redirect('/blog')
            else:
                self.redirect('/blog')

        # Logged out users are redirected to the login page
        else:
            self.redirect('/signin')
