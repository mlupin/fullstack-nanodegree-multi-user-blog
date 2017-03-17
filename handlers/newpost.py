from handlers.blog import BlogHandler
from models.post import Post
from helpers import *


class NewPost(BlogHandler):
    def get(self):
        # Logged in users can create new posts
        if self.user:
            self.render("newpost.html")
        # Logged out users are redirected to the login page
        else:
            self.redirect('/blog')

    def post(self):
        subject = self.request.get('subject')
        content = self.request.get('content')

        # Users can only submit a post if it has a subject and content
        if subject and content:
            author = self.user.name
            p = Post(parent=blog_key(), subject=subject,
                     content=content, author=author,
                     user_id=self.user.key().id())
            p.put()
            self.redirect('/%s' % str(p.key().id()))
        else:
            error = "subject and content, please!"
            self.render("newpost.html", subject=subject, content=content,
                        error=error)
