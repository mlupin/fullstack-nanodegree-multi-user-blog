from handlers.blog import BlogHandler


class MainPage(BlogHandler):
    def get(self):
        return self.render("home.html")
