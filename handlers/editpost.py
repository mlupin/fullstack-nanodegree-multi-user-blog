from handlers.blog import BlogHandler
from google.appengine.ext import db
from helpers import *
import time


class EditPost(BlogHandler):
    def get(self, post_id):
        if self.user:
            key = db.Key.from_path('Post', int(post_id), parent=blog_key())
            post = db.get(key)
            if post and post.user_id == self.user.key().id():
                self.render('editpost.html',
                            subject=post.subject,
                            content=post.content)
            else:
                self.redirect('/blog')
        else:
            self.redirect('/signin')

    def post(self, post_id):
        if not self.user:
            self.redirect('/blog')

        subject = self.request.get('subject')
        content = self.request.get('content')

        if subject and content:
            key = db.Key.from_path('Post', int(post_id), parent=blog_key())
            post = db.get(key)
            post.subject = subject
            post.content = content
            post.put()
            self.redirect('/%s' % post_id)
        else:
            error = "subject and content, please!"
            self.render("editpost.html", subject=subject,
                        content=content, error=error)
