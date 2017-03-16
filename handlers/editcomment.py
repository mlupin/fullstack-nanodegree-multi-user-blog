from handlers.blog import BlogHandler
from google.appengine.ext import db
from helpers import *
from models.comment import Comment
from models.post import Post

import time


class EditComment(BlogHandler):
    def get(self, post_id, user_id, comment_id):
        if self.user:
            postkey = db.Key.from_path('Post', int(post_id), parent=blog_key())
            commentkey = db.Key.from_path('Comment', int(comment_id), parent=postkey)
            comment = db.get(commentkey)
            if comment and comment.user_id == self.user.key().id():
                self.render('editcomment.html',
                            content=comment.content)
            else:
                self.redirect('/blog')
        else:
            self.redirect('/signin')

    def post(self, post_id, user_id, comment_id):
        if not self.user:
            self.redirect('/blog')

        content = self.request.get('content')

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
