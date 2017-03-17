from handlers.blog import BlogHandler
from google.appengine.ext import db
from helpers import *
import time


class EditPost(BlogHandler):
    def get(self, post_id):
        # Logged in users can edit posts
        if self.user:
            key = db.Key.from_path('Post', int(post_id), parent=blog_key())
            post = db.get(key)

            # Users can only edit posts they themselves have made
            if post and post.user_id == self.user.key().id():
                self.render('editpost.html',
                            subject=post.subject,
                            content=post.content)
            else:
                self.redirect('/blog')
        # Logged out users are redirected to the login page
        else:
            self.redirect('/signin')

    def post(self, post_id):
        if not self.user:
            self.redirect('/blog')

        subject = self.request.get('subject')
        content = self.request.get('content')

        # Users can only submit a post if it has a subject and content
        if subject and content:
            key = db.Key.from_path('Post', int(post_id), parent=blog_key())
            post = db.get(key)
            post.subject = subject
            post.content = content
            post.put()
            self.redirect('/blog')
        else:
            error = "subject and content, please!"
            self.render("editpost.html", subject=subject,
                        content=content, error=error)
