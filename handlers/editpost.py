from handlers.blog import BlogHandler
from google.appengine.ext import db
from helpers import *
import time


class EditPost(BlogHandler):
    @signin_required
    def get(self, post_id):
        """
        Redirects user to edit page if the post exists and if the user is
        the author of the post.
        """
        key = db.Key.from_path('Post', int(post_id), parent=blog_key())
        post = db.get(key)

        if post is not None and post.user_id == self.user.key().id():
            return self.render('editpost.html', subject=post.subject,
                               content=post.content)
        else:
            return self.redirect('/blog')

    @signin_required
    def post(self, post_id):
        """
        Updates post if it exists, if user is the author of the post, and
        if content and subject are not none.
        Redirects user to blog page after updating the post.
        """
        subject = self.request.get('subject')
        content = self.request.get('content')

        key = db.Key.from_path('Post', int(post_id), parent=blog_key())
        post = db.get(key)

        if post is not None and post.user_id == self.user.key().id():
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