from handlers.blog import BlogHandler
from models.post import Post
from models.comment import Comment
from models.like import Like
from google.appengine.ext import db


class BlogFront(BlogHandler):
    def get(self):
        # Logged out users are redirected to the home page
        if self.user:
            # Show from newest-oldest posts
            posts = greetings = Post.all().order('-created')
            # Show from oldest-newest comments
            comments = replies = Comment.all().order('created')
            likes = hearts = Like.all().order('created')
            return self.render('front.html', posts=posts, comments=comments,
                               likes=likes)

        elif not self.user:
            return self.render("home.html")
