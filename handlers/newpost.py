from handlers.blog import BlogHandler
from models.post import Post
from helpers import *


class NewPost(BlogHandler):
    @signin_required
    def get(self):
        """
        Renders newpost page if user is signed in
        """
        return self.render("newpost.html")

    @signin_required
    def post(self):
        """
        User must be signed in to create a post.
        Renders blog page with new post if subject and content are not none.
        Renders newpost page with error if subject or content is none.
        """
        subject = self.request.get('subject')
        content = self.request.get('content')

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
