from handlers.blog import BlogHandler
from google.appengine.ext import db
from models.like import Like
from helpers import *
import time


class UnlikePost(BlogHandler):
    @signin_required
    def get(self, post_id):
        """
        User must be signed in to unlike a post.
        Updates like count if the post exists and if user like the post.
        """
        key = db.Key.from_path('Post', int(post_id), parent=blog_key())
        post = db.get(key)

        if post is not None:
            user_id = self.user.key().id()
            post_id = post.key().id()

            like = Like.all().filter('user_id =', user_id).filter(
                                     'post_id =', post_id).get()

            if like and like.user_id == self.user.key().id():
                like.delete()
                post.likes -= 1
                post.put()
                time.sleep(0.1)
                return self.redirect('/blog')
            else:
                return self.redirect('/blog')
        else:
            return self.redirect('/blog')
