from handlers.blog import BlogHandler
from models.user import User


class Signin(BlogHandler):
    def get(self):
        self.render('signin-form.html')

    def post(self):
        username = self.request.get('username')
        password = self.request.get('password')

        user = User.signin(username, password)
        if user:
            self.signin(user)
            self.redirect('/blog')
        else:
            msg = 'Invalid login'
            self.render('signin-form.html', error=msg)
