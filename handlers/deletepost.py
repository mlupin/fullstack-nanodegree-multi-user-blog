from handlers.blog import BlogHandler
from google.appengine.ext import db
from helpers import *

class DeletePost(BlogHandler):
    def get(self, post_id, post_user_id):
        # If user is signed in and the author then delete post
        if self.user and self.user.key().id() == int(post_user_id):
            key = db.key.from_path('Post', int(post_id), parent=blog_key())
            post = db.get(key)
            post.delete()
            self.redirect('/blog')
        elif self.user:
            error = "You don't have permission to delete this post"
            self.render("permalink.html", post=post, error=error)
        else:
            self.redirect('/signin')