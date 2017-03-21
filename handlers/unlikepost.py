from handlers.blog import BlogHandler
from google.appengine.ext import db
from models.like import Like
from helpers import *
import time


class UnlikePost(BlogHandler):
    @signin_required
    def get(self, post_id):
        key = db.Key.from_path('Post', int(post_id), parent=blog_key())
        post = db.get(key)

        # Logged in users can unlike a post if a post exists
        if post:
            user_id = self.user.key().id()
            post_id = post.key().id()

            like = Like.all().filter('user_id =', user_id).filter(
                                     'post_id =', post_id).get()

            # Logged in users can only unlike posts if they already liked it
            if like and like.user_id == self.user.key().id():
                # Cannot dislike a post if it has 0 likes
                # Decrease likes count by 1
                like.delete()
                post.likes -= 1
                post.put()
                time.sleep(0.1)
                return self.redirect('/blog')
            else:
                return self.redirect('/blog')
        elif not post:
            return self.redirect('/blog')
