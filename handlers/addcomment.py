from handlers.blog import BlogHandler
from google.appengine.ext import db
from helpers import *
from models.comment import Comment
import time


class AddComment(BlogHandler):
    @login_required
    def get(self, post_id, user_id):
        """
        Renders addcomment page if user is signed in
        """
        return self.render('addcomment.html')

    @login_required
    def post(self, post_id, user_id):
        """
        Renders blog page with new comment if comment is not none.
        Renders addcomment page with error if content is none.
        """
        content = self.request.get('content')

        if content:
            author = self.user.name
            key = db.Key.from_path('Post', int(post_id), parent=blog_key())
            comment = Comment(parent=key, user_id=int(user_id),
                              post_id=int(post_id), content=content,
                              author=author)
            comment.put()
            time.sleep(0.1)
            return self.redirect('/blog')
        else:
            error = "content, please!"
            return self.render("addcomment.html",
                               content=content, error=error)
