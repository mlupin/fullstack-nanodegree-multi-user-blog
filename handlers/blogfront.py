from handlers.blog import BlogHandler
from models.post import Post
from google.appengine.ext import db


class BlogFront(BlogHandler):
    def get(self):
        #posts  = greetings = Post.all().order('-created')
        posts = db.GqlQuery(
          "select * from Post order by created desc limit 10")

        self.render('front.html', posts=posts)
