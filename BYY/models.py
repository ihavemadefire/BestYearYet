from BYY import db, login_manager
from datetime import datetime
from flask_restful import Resource, Api
from BYY import app

from werkzeug.security import generate_password_hash,check_password_hash
from flask_login import UserMixin
api = Api(app)
@login_manager.user_loader
def load_user(user_id):
    return User.query.get(user_id)

#######################################
###           Set up Tables         ###
#######################################
class User (db.Model, UserMixin):

    __tablename__ = "users"

    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(64),unique=True,index=True)
    username =db.Column(db.String(64),unique=True, index=True)
    password_hash = db.Column(db.String(128))

    def __init__(self,email,username,password):
        self.email = email
        self.username = username
        self.password_hash = generate_password_hash(password)

    def check_password(self,password):
        return check_password_hash(self.password_hash, password)

class Goal(db.Model):

    __tablename__ ='goal'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.Text,nullable=False)
    area = db.Column(db.Text,nullable=False)
    type = db.Column(db.Text,nullable=False)
    description = db.Column(db.Text,nullable=False)
    status = db.Column(db.Text,nullable=False)
    update_news = db.Column(db.Text,nullable=False)
    percent_complete = db.Column(db.Integer, default=0)

    def __init__(self,name,area,type,description,status,update_news,percent_complete):
        self.name= name
        self.area = area
        self.type = type
        self.description = description
        self.status = status
        self.update_news = update_news
        self.percent_complete = percent_complete

    def json(self):

        return {'name':self.name,'area':self.area,'type':self.type,'description':self.description,'status':self.status,'update_news':self.update_news,'percent_complete':self.percent_complete}


    def __repr__(self):
        return f"{self.name}"

class Blog(db.Model):

    __tablename__ ='blog'
    id = db.Column(db.Integer, primary_key=True)
    blog_name = db.Column(db.String(200))
    date = db.Column(db.DateTime,nullable=False,default=datetime.utcnow)
    cover_image = db.Column(db.String(64))
    subtitle = db.Column(db.String (160))
    subject = db.Column(db.String (160),nullable=False)
    text = db.Column(db.Text,nullable=False)


    def __init__(self,subject,subtitle,cover_image,text, blog_name):
        self.subject = subject
        self.subtitle = subtitle
        self.cover_image = cover_image
        self.text = text
        self.blog_name = blog_name


    def __repr__(self):
        return f"{self.date}, {self.subject} "

class Book(db.Model):

    __tablename__ ='book'
    id = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.DateTime,nullable=False,default=datetime.utcnow)
    title = db.Column(db.Text,nullable=False)
    language = db.Column(db.Text,nullable=False)
    author = db.Column(db.Text,nullable=False)
    pages = db.Column(db.Integer,nullable=False)
    f_nf = db.Column(db.String(12),nullable=False)
    genre = db.Column(db.Text,nullable=False)
    pub_date = db.Column(db.Integer)
    review = db.Column(db.Text,nullable=False)
    cover_image = db.Column(db.String(64))
    headline = db.Column(db.Text, nullable=True)
    book_name= db.Column(db.String(200))

    def __init__(self,title,author,pages,language,f_nf,genre,pub_date,review,cover_image,headline,book_name):
        self.title= title
        self.author = author
        self.language = language
        self.pages = pages
        self.f_nf = f_nf
        self.genre = genre
        self.pub_date = pub_date
        self.review = review
        self.cover_image = cover_image
        self.headline = headline
        self.book_name = book_name

    def __repr__(self):
        return f"{self.title} -- {self.book_name}"

class Health(db.Model):

    __tablename__ ='health'
    id = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.Date,nullable=False,default=datetime.utcnow)
    weight = db.Column(db.Text,nullable=False)
    diastole = db.Column(db.Text,nullable=False)
    systole = db.Column(db.Text,nullable=False)
    bicep = db.Column(db.Text,nullable=False)
    chest = db.Column(db.Text,nullable=False)
    health_name = db.Column(db.Text,nullable=False)
    stomach = db.Column(db.Text,nullable=False)
    waist = db.Column(db.Text,nullable=False)
    hips = db.Column(db.Text,nullable=False)
    progress_image = db.Column(db.String(64))




    def __init__(self,weight,diastole,systole,bicep,chest,stomach,waist,hips, health_name,progress_image):
        self.weight= weight
        self.diastole = diastole
        self.systole = systole
        self.bicep = bicep
        self.chest = chest
        self.stomach = stomach
        self.waist = waist
        self.hips = hips
        self.health_name = health_name
        self.progress_image = progress_image



    def __repr__(self):
        return f"{self.weight}"

class News(db.Model):

    __tablename__ ='news'
    id = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.DateTime,nullable=False,default=datetime.utcnow)
    area = db.Column(db.String (160))
    resolution = db.Column(db.String (160))
    subject = db.Column(db.String (160),nullable=False)
    text = db.Column(db.Text,nullable=False)


    def __init__(self,area,resolution,subject,text):
        self.area = area
        self.resolution = resolution
        self.subject = subject
        self.text = text


    def __repr__(self):
        return f"{self.date}, {self.subject} "

class Goals(Resource):
    def get(self,name):
        goal = Goal.query.filter_by(name=name).first()
        if goal:
            return goal.json()
        else:
            return {'name':none},404

api.add_resource(Goals, '/goals/<string:name>')

class List(Resource):
    def get(self,area):
        goals = Goal.query.filter_by(area=area).with_entities("name").all()
        return [goal.name for goal in goals]

api.add_resource(List, '/areas/<string:area>')
