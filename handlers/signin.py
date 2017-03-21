from handlers.blog import BlogHandler
from models.user import User


class Signin(BlogHandler):
    def get(self):
        return self.render('signin-form.html')

    def post(self):
        username = self.request.get('username')
        password = self.request.get('password')

        user = User.signin(username, password)
        if user:
            self.signin(user)
            return self.redirect('/blog')
        else:
            error = 'Invalid login'
            return self.render('signin-form.html', error=error)
