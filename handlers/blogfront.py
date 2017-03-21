from handlers.blog import BlogHandler
from helpers import *
from models.post import Post
from models.comment import Comment
from models.like import Like
from google.appengine.ext import db


class BlogFront(BlogHandler):
    @signin_required
    def get(self):
        # Show from newest-oldest posts
        posts = greetings = Post.all().order('-created')
        # Show from oldest-newest comments
        comments = replies = Comment.all().order('created')
        likes = hearts = Like.all().order('created')
        return self.render('front.html', posts=posts, comments=comments,
                           likes=likes)
