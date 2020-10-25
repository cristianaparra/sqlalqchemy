import db

from sqlalchemy import Column, Integer, String, FLoat

class Users(Base):
    __tablename__ = 'users'
   

    id = Column(Integer, primary_key=True)
    name = Column(String(80), nullable=False)
    username = Column(String(80), nullable=False)
    email = Column(String(80), nullable=False)
    password = Column(String(30), nullable=False)



    def serialize(self):
        return {
            "id": self.id,
            "name": self.name
            "username": self.username
            "email": self.email
            "password": self.password
        }


class Likes(Base):
    __tablename__ = 'likes'
 
    id = Column(Integer, primary_key=True)
    user_id = Column(String(50), nullable=False)
    post_id = Column(String(50), nullable=False)
    



    def serialize(self):
        return {
            "id": self.id,
            "user_id": self.user_id
            "post_id": self.post_id
        }

class Post(Base):
    __tablename__ = 'post'
 
    id = Column(Integer, primary_key=True)
    user_id = Column(String(50), nullable=False)
    photo = Column(String(250), nullable=False)
    description = Column(String)
    created_at = Column(String(80), nullable=False)
    updated_at = Column(String(80), nullable=False)



    def serialize(self):
        return {
            "id": self.id,
            "user_id": self.user_id
            "photo": self.photo
            "description": self.description
            "created_at": self.created_at
            "updated_at": self.updated_at
        }

class Comments(Base):
    __tablename__ = 'comments'

    id = Column(Integer, primary_key=True)
    user_id = Column(String(50), nullable=False)
    post_id = Column(String(50), nullable=False)
    content = Column(String(250), nullable=False)
    created_at = Column(String(80), nullable=False)
    update_at = Column(String(90), nullable=False)
   



    def serialize(self):
        return {
            "id": self.id,
            "user_id": self.user_id
            "post_id": self.post_id
            "content": self.content
            "created_at": self.created_at
            "updated_at": self.updated_at
        }
class Followers(Base):
    __tablename__ = 'followers'

    id = Column(Integer, primary_key=True)
    follower_id = Column(String(80), nullable=False)
    user_id = Column(String(80), nullable=False)
    accepted = Column(Boolean(False))
    



    def serialize(self):
        return {
            "id": self.id,
            "follower_id": self.follower_id
            "user_id": self.user_id
            "accepted": self.accepted
        }