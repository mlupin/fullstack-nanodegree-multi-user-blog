from handlers.blog import BlogHandler
from google.appengine.ext import db
from helpers import *
from models.comment import Comment
from models.post import Post

import time


class EditComment(BlogHandler):
    def get(self, post_id, user_id, comment_id):
        # Logged in users can edit comments
        if self.user:
            postkey = db.Key.from_path('Post', int(post_id), parent=blog_key())
            commentkey = db.Key.from_path('Comment', int(comment_id), parent=postkey)
            comment = db.get(commentkey)
            
            # Users can only edit comments they themselves have made
            if comment and comment.user_id == self.user.key().id():
                self.render('editcomment.html',
                            content=comment.content)
            else:
                self.redirect('/blog')
        # Logged out users are redirected to the login page
        else:
            self.redirect('/signin')

    def post(self, post_id, user_id, comment_id):
        if not self.user:
            self.redirect('/blog')

        content = self.request.get('content')

        # Users can only edit a comment if comment has content
        if content:
            postkey = db.Key.from_path('Post', int(post_id), parent=blog_key())
            commentkey = db.Key.from_path('Comment', int(comment_id), parent=postkey)
            comment = db.get(commentkey)
            comment.content = content
            comment.put()
            time.sleep(0.1)
            self.redirect('/blog')
        else:
            error = "content, please!"
            self.render("editcomment.html.html", content=content, error=error)
