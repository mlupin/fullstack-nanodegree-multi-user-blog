from handlers.blog import BlogHandler
from google.appengine.ext import db
from helpers import *
from models.post import Post
from models.comment import Comment
import time


class DeleteComment(BlogHandler):
    @signin_required
    def get(self, post_id, user_id, comment_id):
        # Logged in users can delete comments
        postkey = db.Key.from_path('Post', int(post_id), parent=blog_key())
        commentkey = db.Key.from_path('Comment', int(comment_id),
                                      parent=postkey)
        comment = db.get(commentkey)

        # Users can only delete comments they themselves have made
        if comment and self.user.key().id() == int(comment.user_id):
            comment.delete()
            time.sleep(0.1)
            return self.redirect('/blog')
        else:
            return self.redirect('/blog')
