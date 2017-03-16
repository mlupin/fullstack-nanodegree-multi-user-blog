from handlers.blog import BlogHandler
from google.appengine.ext import db
from models.like import Like
from helpers import *
import time


class UnlikePost(BlogHandler):
    def get(self, post_id):
        key = db.Key.from_path('Post', int(post_id), parent=blog_key())
        post = db.get(key)

        if self.user and post:
            user_id = self.user.key().id()
            post_id = post.key().id()

            like = Like.all().filter('user_id =', user_id).filter('post_id =', post_id).get()

            if like and like.user_id == self.user.key().id():
                # cannot dislike a post if it has 0 likes
                like.delete()
                post.likes -= 1
                post.put()
                time.sleep(0.1)
                self.redirect('/blog')
            else:
                self.redirect('/blog')


        else:
            self.redirect('/signin')
