from handlers.blog import BlogHandler


class MainPage(BlogHandler):
    def get(self):
        self.render("home.html")
