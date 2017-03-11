from handlers.blog import BlogHandler
from models.user import User


class Signin(BlogHandler):
    def get(self):
        self.render('signin-form.html')

    def post(self):
        username = self.request.get('username')
        password = self.request.get('password')

        if User.signin(username, password):
            self.signin(User.signin(username, password))
            self.redirect('/blog')
        else:
            message = 'Invalid login'
            self.render('signin-form.html', error=message)
