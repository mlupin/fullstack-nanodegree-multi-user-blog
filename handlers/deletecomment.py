from handlers.blog import BlogHandler
from google.appengine.ext import db
from helpers import *
from models.post import Post
from models.comment import Comment
import time


class DeleteComment(BlogHandler):
    @signin_required
    def get(self, post_id, user_id, comment_id):
        """
        User must be signed in to delete a comment.
        Deletes comment if it exists and if user is the author of the comment.
        Redirects user to blog page after deleting comment.
        """
        postkey = db.Key.from_path('Post', int(post_id), parent=blog_key())
        commentkey = db.Key.from_path('Comment', int(comment_id),
                                      parent=postkey)
        comment = db.get(commentkey)

        if comment is not None and self.user.key().id() == int(comment.user_id):
            comment.delete()
            time.sleep(0.1)
            return self.redirect('/blog')
        else:
            return self.redirect('/blog')
