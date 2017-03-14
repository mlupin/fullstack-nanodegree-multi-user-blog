import webapp2
from google.appengine.ext import db
from helpers import *


from handlers.blog import BlogHandler
from handlers.blogfront import BlogFront
from handlers.mainpage import MainPage
from handlers.newpost import NewPost
from handlers.deletepost import DeletePost
from handlers.editpost import EditPost
from handlers.postpage import PostPage
from handlers.signup import Signup
from handlers.signin import Signin
from handlers.signout import Signout


from models.post import Post
from models.user import User


app = webapp2.WSGIApplication([('/', MainPage),
                               ('/blog', BlogFront),
                               ('/([0-9]+)', PostPage),
                               ('/newpost', NewPost),
                               ('/([0-9]+)/delete/([0-9]+)', DeletePost),
                               ('/([0-9]+)/edit/([0-9]+)', EditPost),
                               ('/signup', Signup),
                               ('/signin', Signin),
                               ('/signout', Signout)
                               ],
                              debug=True)
