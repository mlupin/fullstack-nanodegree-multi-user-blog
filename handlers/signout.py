from handlers.blog import BlogHandler


class Signout(BlogHandler):
    def get(self):
        self.signout()
        self.redirect('/blog')
