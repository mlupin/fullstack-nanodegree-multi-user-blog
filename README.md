# Multi User Blog

This projects is part of the Udacity Full Stack Web Developer Nanodegree. This project was build on top of the blog created in the Intro the Backend course.

Blog: [https://blog-160005.appspot.com/](https://blog-160005.appspot.com/)

### Basic features

* Users can sign up and sign in to create their own posts.
* Only signed in users can view, create, update, delete posts and comments.

### Additional features

* Users can write, update, and delete posts
* Users can like other users' posts

### TODO List

* Refactor: save likes in the Post model as ListProperty to save the user_id of the user that has liked the page. Then calculate the number of likes using len method and check if the author has liked a specific post by checking if current_user_id in post.likes conditional.
* Add third party authentication and sign in with Google or Facebook
* Create a sort feature to sort posts by author, date created, date updated, most likes, most comments
* Add category tags to posts

### Current Issues

* Like and dislike buttons are showing even if the user already liked or disliked the post

### Installation
Clone the [fullstack-nanodegree-blog](https://github.com/mlupin/udacity-multi-user-blog) repository and run the application on your local machine.
```
$ git clone https://github.com/mlupin/udacity-multi-user-blog.git
$ cd udacity-multi-user-blog
$ dev_appserver.py .
```

### Recognition
Login template code and design obtained from Colorlib: [Transparent Form With Logo](https://colorlib.com/wp/html5-and-css3-login-forms/). Download [here](http://codepen.io/motorlatitude/share/zip/JFkro/)
