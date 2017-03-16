from handlers.blog import BlogHandler
from google.appengine.ext import db
from models.like import Like
from helpers import *
import time


class UnlikePost(BlogHandler):
    def get(self, post_id):
        key = db.Key.from_path('Post', int(post_id), parent=blog_key())
        post = db.get(key)

        if self.user:
            user_id = self.user.key().id()
            post_id = post.key().id()

            like = Like.all().filter('user_id =', user_id).filter('post_id =', post_id).get()

            if like:
                #self.redirect('/%s' % str(post.key().id()))
                self.redirect('/blog')

            else:
                like = Like(parent=key, 
                            user_id=self.user.key().id(),
                            post_id=post.key().id())

                post.likes += 1

                like.put()
                post.put()

                #self.redirect('/%s' % str(post.key().id()))
                self.redirect('/blog')
        else:
            self.redirect('/signin')
