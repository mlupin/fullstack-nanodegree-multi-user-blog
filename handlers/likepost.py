from handlers.blog import BlogHandler
from google.appengine.ext import db
from models.like import Like
from helpers import *
import time


class LikePost(BlogHandler):
    def get(self, post_id):
        key = db.Key.from_path('Post', int(post_id), parent=blog_key())
        post = db.get(key)

        if self.user:
            # User cannot like thier own posts
            if post.user_id == self.user.key().id():
                error = "You cannot like your own post!"
                self.render("base.html", access_error=error)
            else:
                user_id = self.user.key().id()
                post_id = post.key().id()
                like = Like.all().filter('user_id =', user_id).filter('post_id =', post_id).get()           

                # User can only like a post once
                if like:
                    self.redirect('/blog')

                else:
                    like = Like(parent=key, 
                                user_id=self.user.key().id(),
                                post_id=post.key().id())

                    post.likes += 1
                    like.put()
                    post.put()
                    time.sleep(0.1)
                    self.redirect('/blog')
        else:
            self.redirect('/signin')
