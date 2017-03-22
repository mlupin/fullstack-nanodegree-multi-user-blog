from handlers.blog import BlogHandler


class Logout(BlogHandler):
    def get(self):
        self.logout()
        return self.redirect('/')
