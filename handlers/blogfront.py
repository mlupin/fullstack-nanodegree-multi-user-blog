from handlers.blog import BlogHandler
from models.post import Post
from google.appengine.ext import db


class BlogFront(BlogHandler):
    def get(self):
        if self.user:
            posts = greetings = Post.all().order('-created')
            self.render('front.html', posts=posts)

        else:
            self.render("home.html")