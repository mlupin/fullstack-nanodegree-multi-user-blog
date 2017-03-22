import webapp2
from models.user import User
from helpers import *


class BlogHandler(webapp2.RequestHandler):
    def write(self, *a, **kw):
        """
        Writes output to client browser.
        """
        self.response.out.write(*a, **kw)

    def render_str(self, template, **params):
        """
        Renders html using template.
        """
        params['user'] = self.user
        return render_str(template, **params)

    def render(self, template, **kw):
        """
        Writes the html template to client browser
        """
        self.write(self.render_str(template, **kw))

    def set_secure_cookie(self, name, val):
        """
        Sets secure cookie to browser.
        """
        cookie_val = make_secure_val(val)
        self.response.headers.add_header(
            'Set-Cookie',
            '%s=%s; Path=/' % (name, cookie_val))

    def login(self, user):
        """
        Verifies user existance.
        """
        self.set_secure_cookie(
            'user_id',
            str(user.key().id()))

    def logout(self):
        """
        Resets cookie.
        """
        self.response.headers.add_header(
            'Set-Cookie',
            'user_id=; Path=/')

    def initialize(self, *a, **kw):
        """
        Verfies user login status using cookie information.
        """
        webapp2.RequestHandler.initialize(self, *a, **kw)
        uid = self.read_secure_cookie('user_id')
        self.user = uid and User.by_id(int(uid))

    def read_secure_cookie(self, name):
        """
        Reads secure cookie to browser.
        """
        cookie_val = self.request.cookies.get(name)
        return cookie_val and check_secure_val(cookie_val)
