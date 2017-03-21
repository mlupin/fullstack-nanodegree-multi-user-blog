# Multi User Blog

This projects is part of the Udacity Full Stack Web Developer Nanodegree. This project was build on top of the blog created in the Intro the Backend course.

Blog: [https://blog-160005.appspot.com/](https://blog-160005.appspot.com/)

### Prerequisites and Installing
Clone the [fullstack-nanodegree-blog](https://github.com/mlupin/udacity-multi-user-blog) repository and run the application on your local machine
  ```
  git clone https://github.com/mlupin/udacity-multi-user-blog.git
  cd udacity-multi-user-blog
  dev_appserver.py .
  ```

### Recognition
Login template code and design obtained from Colorlib: Transparent Form With Logo
https://colorlib.com/wp/html5-and-css3-login-forms/
To download: http://codepen.io/motorlatitude/share/zip/JFkro/

###TODO
Need to save likes in the Post model as ListProperty to save the user_id of the user that has liked the page. Then calculate the number of likes using len method and check if the author has liked a specific post by checking if current_user_id in post.likes conditional.