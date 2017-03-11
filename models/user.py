from google.appengine.ext import db
from helpers import *


class User(db.Model):
    username = db.StringProperty(required=True)
    name = db.StringProperty(required=True)
    pw_hash = db.StringProperty(required=True)
    email = db.StringProperty(required=True)
    salt = db.StringProperty(required=True)

    @classmethod
    def by_id(cls, uid):
        return User.get_by_id(uid)

    @classmethod
    def by_username(cls, username):
        return User.all().filter('username =', username).get()

    @classmethod
    def by_email(cls, email):
        return User.all().filter('email =', email).get()

    @classmethod
    def register(cls, username, name, pw, email, salt, pw_hash):
        if User.by_username(username):
            return False
        else:
            return User(username=username,
                        name=name,
                        pw_hash=pw_hash,
                        email=email,
                        salt=salt
                        )

    @classmethod
    def signin(cls, name, pw):
        u = cls.by_name(name)
        if u and valid_pw(name, pw, u.pw_hash):
            return u