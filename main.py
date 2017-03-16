import webapp2
from google.appengine.ext import db
from helpers import *


from handlers.blog import BlogHandler
from handlers.blogfront import BlogFront
from handlers.mainpage import MainPage
from handlers.postpage import PostPage
from handlers.newpost import NewPost
from handlers.editpost import EditPost
from handlers.deletepost import DeletePost
from handlers.likepost import LikePost
from handlers.unlikepost import UnlikePost
from handlers.addcomment import AddComment
from handlers.editcomment import EditComment
from handlers.deletecomment import DeleteComment
from handlers.signup import Signup
from handlers.signin import Signin
from handlers.signout import Signout

from models.user import User
from models.post import Post
from models.like import Like
from models.comment import Comment


app = webapp2.WSGIApplication([('/', MainPage),
                               ('/blog', BlogFront),
                               ('/newpost', NewPost),
                               ('/([0-9]+)', PostPage),
                               ('/([0-9]+)/delete', DeletePost),
                               ('/([0-9]+)/edit', EditPost),
                               ('/([0-9]+)/like', LikePost),
                               ('/([0-9]+)/unlike', UnlikePost),
                               ('/([0-9]+)/([0-9]+)/addcomment', AddComment),
                               ('/([0-9]+)/([0-9]+)/([0-9]+)/editcomment', EditComment),
                               ('/([0-9]+)/([0-9]+)/([0-9]+)/deletecomment', DeleteComment),
                               ('/signup', Signup),
                               ('/signin', Signin),
                               ('/signout', Signout),
                               ('/blog/?', BlogFront),
                               ],
                              debug=True)
