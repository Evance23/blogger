from . import db ,login_manager
from datetime import datetime
from werkzeug.security import generate_password_hash,check_password_hash 
from werkzeug.utils import secure_filename
from werkzeug.datastructures import  FileStorage 
from flask_login import UserMixin , current_user

class User(UserMixin, db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(255), unique=True)
    email = db.Column(db.String(255), unique=True)
    password = db.Column(db.String(255))

    def save(self):
        db.session.add(self)
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()

    @property
    def set_password(self):
        # raise AttributeError('You cannot read the password attribute') 
        pass 
    # @set_password.setter
    # def password(self, password):
    #     self.secure_password = generate_password_hash(password)
        
        
    def check_password(self, password):
        
        # return check_password_hash(self.password, password) 
        print(self.email)
        print(self.password)
        print(self.id)
        print(self.username)
        print(password)
        return self.password == password

    def __repr__(self):
        return f'User: {self.username}'


    @login_manager.user_loader
    def user_loader(user_id):
        return User.query.get(user_id)

# class Categories(db.Model):
#     art = db.Column(db.string)
#     music = db.Column(db.string)
#     poetry = db.Column(db.string) 
    
class Post(db.Model):
    __tablename__ = 'posts'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String, nullable=False)
    user_id = db.Column(db.String, nullable=False)
    post = db.Column(db.String, nullable=False)
    comment = db.relationship('Comment',  lazy='dynamic')
    category = db.Column(db.String, nullable=False) 
    date_created = db.Column(db.DateTime, default=datetime.utcnow)
    # up_vote = db.relationship('Upvote', lazy='dynamic')
    # down_vote = db.relationship('Downvote', lazy='dynamic')
    # backref='post' 

    def save(self):
        db.session.add(self)
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()

    def __repr__(self):
        return f"Post Title: {self.title}"


class Comment(db.Model):
    __tablename__ = 'comments'
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    post_id = db.Column(db.Integer, db.ForeignKey('posts.id'), nullable=False)
    comment = db.Column(db.Text())

    def save(self):
        db.session.add(self)
        db.session.commit()

    @classmethod
    def get_comments(cls, post_id):
        comments = Comment.query.filter_by(post_id=post_id).all()
        return comments

    def delete(self):
        db.session.delete(self)
        db.session.commit()

    def __repr__(self):
        return f'Comments: {self.comment}'


class Upvote(db.Model):
    __tablename__ = 'upvotes'
    id = db.Column(db.Integer, primary_key=True)
    upvote = db.Column(db.Integer, default=1)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    post_id = db.Column(db.Integer, db.ForeignKey('posts.id'))

    def save(self):
        db.session.add(self)
        db.session.commit()

    def upvote(cls, id):
        upvote_post = Upvote(user=current_user, post_id=id)
        upvote_post.save()

    @classmethod
    def query_upvotes(cls, id):
        upvote = Upvote.query.filter_by(post_id=id).all()
        return upvote

    @classmethod
    def all_upvotes(cls):
        upvotes = Upvote.query.order_by('id').all()
        return upvotes

    def __repr__(self):
        return f'{self.user_id}:{self.post_id}'


class Downvote(db.Model):
    __tablename__ = 'downvotes'
    id = db.Column(db.Integer, primary_key=True)
    downvote = db.Column(db.Integer, default=1)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    post_id = db.Column(db.Integer, db.ForeignKey('posts.id'))

    def save(self):
        db.session.add(self)
        db.session.commit()

    def downvote(cls, id):
        downvote_post = Downvote(user=current_user, post_id=id)
        downvote_post.save()

    @classmethod
    def query_downvotes(cls, id):
        downvote = Downvote.query.filter_by(post_id=id).all()
        return downvote

    @classmethod
    def all_downvotes(cls):
        downvote = Downvote.query.order_by('id').all()
        return downvote

    def __repr__(self):
        return f'{self.user_id}:{self.post_id}'
