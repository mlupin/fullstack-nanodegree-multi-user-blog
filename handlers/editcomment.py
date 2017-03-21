from handlers.blog import BlogHandler
from google.appengine.ext import db
from helpers import *
from models.comment import Comment
from models.post import Post

import time


class EditComment(BlogHandler):
    @signin_required
    def get(self, post_id, user_id, comment_id):
        # Logged in users can edit comments
        postkey = db.Key.from_path('Post', int(post_id), parent=blog_key())
        commentkey = db.Key.from_path('Comment', int(comment_id),
                                      parent=postkey)
        comment = db.get(commentkey)

        # Users can only edit comments they themselves have made
        if comment and self.user.key().id() == int(comment.user_id):
                return self.render('editcomment.html', content=comment.content)
        else:
            return self.redirect('/blog')

    @signin_required
    def post(self, post_id, user_id, comment_id):
        content = self.request.get('content')
        postkey = db.Key.from_path('Post', int(post_id), parent=blog_key())
        commentkey = db.Key.from_path('Comment', int(comment_id),
                                      parent=postkey)
        comment = db.get(commentkey)

        # Users can only edit a comment if comment has content
        if comment and self.user.key().id() == int(comment.user_id):
            if content:
                comment.content = content
                comment.put()
                time.sleep(0.1)
                return self.redirect('/blog')
            else:
                error = "content, please!"
                return self.render("editcomment.html", content=content,
                                   error=error)
        else:
            return self.redirect('/blog')
