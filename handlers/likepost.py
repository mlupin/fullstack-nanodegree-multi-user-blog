from handlers.blog import BlogHandler
from google.appengine.ext import db
from models.like import Like
from helpers import *
import time


class LikePost(BlogHandler):
    @signin_required
    def get(self, post_id):
        # User cannot like their own posts
        key = db.Key.from_path('Post', int(post_id), parent=blog_key())
        post = db.get(key)

        if post is not None:
            if post.user_id == self.user.key().id():
                error = "You cannot like your own post!"
                return self.render("base.html", access_error=error)
            else:
                user_id = self.user.key().id()
                post_id = post.key().id()
                like = Like.all().filter('user_id =', user_id).filter(
                                         'post_id =', post_id).get()

                # User can only like a post once
                # TODO: raise an error if a user already like a post
                if like:
                    return self.redirect('/blog')
                else:
                    like = Like(parent=key,
                                user_id=self.user.key().id(),
                                post_id=post.key().id())

                    post.likes += 1
                    like.put()
                    post.put()
                    time.sleep(0.1)
                    return self.redirect('/blog')
        else:
            return self.redirect('/blog')
