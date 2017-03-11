import webapp2
from google.appengine.ext import db
from helpers import *


from handlers.blog import BlogHandler
from handlers.blogfront import BlogFront
from handlers.mainpage import MainPage
from handlers.newpost import NewPost
from handlers.postpage import PostPage
from handlers.register import Register
from handlers.signin import Signin
from handlers.signout import Signout


from models.post import Post
from models.user import User


app = webapp2.WSGIApplication([('/', MainPage),
                               ('/blog/?', BlogFront),
                               ('/blog/([0-9]+)', PostPage),
                               ('/blog/newpost', NewPost),
                               ('/signup', Register),
                               ('/signin', Signin),
                               ('/signout', Signout)
                               ],
                              debug=True)
