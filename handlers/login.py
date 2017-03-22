from handlers.blog import BlogHandler
from models.user import User


class Login(BlogHandler):
    def get(self):
        return self.render('login-form.html')

    def post(self):
        username = self.request.get('username')
        password = self.request.get('password')

        user = User.login(username, password)
        if user:
            self.login(user)
            return self.redirect('/blog')
        else:
            error = 'Invalid login'
            return self.render('login-form.html', error=error)
