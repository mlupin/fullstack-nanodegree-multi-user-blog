from handlers.blog import BlogHandler
from models.post import Post
from models.comment import Comment
from google.appengine.ext import db


class BlogFront(BlogHandler):
    def get(self):
        if self.user:
            posts = greetings = Post.all().order('-created')
            comments = replies = Comment.all().order('created')
            self.render('front.html', posts=posts, comments=comments)

        else:
            self.render("home.html")
