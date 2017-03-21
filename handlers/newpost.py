from handlers.blog import BlogHandler
from models.post import Post
from helpers import *


class NewPost(BlogHandler):
    @signin_required
    def get(self):
        # Logged in users can create new posts
        return self.render("newpost.html")

    @signin_required
    def post(self):
        # Logged in users can create new posts
        subject = self.request.get('subject')
        content = self.request.get('content')

        # Users can only submit a post if it has a subject and content
        if subject and content:
            author = self.user.name
            post = Post(parent=blog_key(), subject=subject,
                        content=content, author=author,
                        user_id=self.user.key().id())
            post.put()
            return self.redirect('/%s' % str(post.key().id()))
        else:
            error = "subject and content, please!"
            return self.render("newpost.html", subject=subject,
                               content=content, error=error)
