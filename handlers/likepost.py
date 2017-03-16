from handlers.blog import BlogHandler
from google.appengine.ext import db
from models.like import Like
from helpers import *
import time


class LikePost(BlogHandler):
    def get(self, post_id):
        if self.user and post.user_id == self.user.key().id():
                error = "Sorry, you cannot like your own post."
                self.render('base.html', access_error=error)
        elif not post.user_id == self.user.key().id():
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
