from handlers.blog import BlogHandler
from google.appengine.ext import db
from helpers import *
from models.post import Post
from models.comment import Comment
import time


class DeleteComment(BlogHandler):
    def get(self, post_id, user_id, comment_id):
        if self.user:  # If user is signed in
            commentkey = db.Key.from_path('Comment', int(comment_id), parent=blog_key())
            comment = db.get(commentkey)
            # If the user is the author of the comment
            if self.user.key().id() == comment.user_id:
                comment.delete()
                time.sleep(0.1)
                self.redirect('/blog')
        elif not self.user:
            self.redirect('/signin')
        else:
            self.write("You don't have permission to delete this comment.")
