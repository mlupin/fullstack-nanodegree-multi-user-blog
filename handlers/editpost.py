from handlers.blog import BlogHandler
from google.appengine.ext import db
from helpers import *
import time


class EditPost(BlogHandler):
    @signin_required
    def get(self, post_id):
        # Logged in users can edit posts
        key = db.Key.from_path('Post', int(post_id), parent=blog_key())
        post = db.get(key)

        # Users can only edit posts they themselves have made
        if post and post.user_id == self.user.key().id():
            return self.render('editpost.html', subject=post.subject,
                               content=post.content)
        else:
            return self.redirect('/blog')

    @signin_required
    def post(self, post_id):
        subject = self.request.get('subject')
        content = self.request.get('content')

        key = db.Key.from_path('Post', int(post_id), parent=blog_key())
        post = db.get(key)

        # Users can only submit a post if it has a subject and content
        if post and post.user_id == self.user.key().id():
            if subject and content:
                key = db.Key.from_path('Post', int(post_id), parent=blog_key())
                post = db.get(key)
                post.subject = subject
                post.content = content
                post.put()
                return self.redirect('/blog')
            else:
                error = "subject and content, please!"
                return self.render("editpost.html", subject=subject,
                                   content=content, error=error)