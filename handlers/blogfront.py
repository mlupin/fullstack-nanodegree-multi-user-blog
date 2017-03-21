from handlers.blog import BlogHandler
from helpers import *
from models.post import Post
from models.comment import Comment
from models.like import Like
from google.appengine.ext import db


class BlogFront(BlogHandler):
    @signin_required
    def get(self):
        """
        Renders the front blog page with users' posts, likes, and comments.
        Posts are sorted from newest-oldest
        Comments are sorted from oldest-newest
        """
        posts = greetings = Post.all().order('-created')
        comments = replies = Comment.all().order('created')
        likes = hearts = Like.all().order('created')
        return self.render('front.html', posts=posts, comments=comments,
                           likes=likes)
