from flask_wtf import FlaskForm
from wtforms import StringField,SubmitField,TextAreaField, SelectField, RadioField,IntegerField, FileField, DateTimeField, PasswordField
from wtforms.validators import DataRequired, Email, EqualTo
from wtforms import ValidationError
from flask_wtf.file import FileField, FileAllowed

#######################################
###           Set up Forms          ###
#######################################


class GoalForm(FlaskForm):
    name = StringField('Goal Name: ', validators=[DataRequired()])
    area = SelectField('Area of Life: ', choices=[('health','Health & Grooming'),('career','Career and Skills'),('home','Home'),('projects','Projects'),('learning','Learning'),('family','Family'),('headspace','Headspace')],validators=[DataRequired()])
    type = RadioField('Type of Goal: ', choices=[('habit','Habit'),('discrete','Discrete Goal')], validators=[DataRequired()])
    description = StringField('Description: ', validators=[DataRequired()])
    status = SelectField('Status: ', choices=[('Not Yet Started','Not Yet Started'),('In Flight','In Flight'),('Online or Complete','Online or Complete')] ,validators=[DataRequired()])
    update_news = StringField('News: ')
    percent_complete= IntegerField('Percent complete: ')
    submit = SubmitField("Submit")

class BlogForm(FlaskForm):
    subject = StringField('Subject: ', validators=[DataRequired()])
    cover_image = FileField('Cover Image: ', validators=[FileAllowed(['jpg','png'])])
    subtitle = StringField('Subtitle: ', validators=[DataRequired()])
    text = TextAreaField('Post: ', validators=[DataRequired()])
    submit = SubmitField("Submit")

class BookForm(FlaskForm):
    title = StringField('Title: ', validators=[DataRequired()])
    author = StringField('Author: ', validators=[DataRequired()])
    pages = IntegerField('Number of pages: ', validators=[DataRequired()])
    language = StringField('Language: ', validators=[DataRequired()])
    f_nf = SelectField('Fiction/Nonfiction: ', choices=[('fiction','Fiction'),('Nonfiction','Nonfiction')],validators=[DataRequired()])
    genre = SelectField('Genre: ',  choices=[('Art','Art'),('Biography','Biography'),('Business & Finance','Business & Finance'),('Graphic Novels','Graphic Novels'),('Computers & Technology','Computers Technology'),('Food','Food'),('Engineering','Engineering'),('Health & Fitness','Health & Fitness'),('History','History'),('Humor','Humor'),('Novels','Novels'),('Classics','Classics'),('Mystery','Mystery'),('Parenting & Relationships','Parenting & Relationships'),('Politics & Social Sciences','Politics & Social Sciences'),('Science & Math','Science & Math'),('SciFi & Fantasy','SciFi & Fantasy'),('Sports & Outdoors','Sports & Outdoors'),('Travel','Travel')] ,validators=[DataRequired()])
    pub_date = IntegerField('Publication Date: ')
    review = TextAreaField('Review: ', validators=[DataRequired()])
    cover_image = FileField('Cover Image: ', validators=[FileAllowed(['jpg','png'])])
    headline = StringField('Headline: ')
    submit = SubmitField("Submit")

class HealthForm(FlaskForm):
    #weight,diastole,systole,bicep,chest,stomach,waist,hip,miles_run,progress_image
    weight = IntegerField('Weight: ', validators=[DataRequired()])
    diastole = IntegerField('Diastole: ', validators=[DataRequired()])
    systole = IntegerField('Systole: ', validators=[DataRequired()])
    bicep = IntegerField('Bicep: ', validators=[DataRequired()])
    chest = IntegerField('Chest: ', validators=[DataRequired()])
    stomach = IntegerField('Stomach: ', validators=[DataRequired()])
    waist = IntegerField('Waist: ', validators=[DataRequired()])
    hips = IntegerField('Hips ', validators=[DataRequired()])
    progress_image = FileField('Progress Image: ', validators=[FileAllowed(['jpg','png'])])
    progress_image = FileField('Progress Image: ', validators=[FileAllowed(['jpg','png'])])
    submit = SubmitField("Submit")

class NewsForm(FlaskForm):
    #area,resoltuion,subject,text
    area = StringField('Title: ', validators=[DataRequired()])
    resolution = StringField('Resoltuion', validators=[DataRequired()])
    subject = StringField('Area: ', validators=[DataRequired()])
    text = TextAreaField('News ', validators=[DataRequired()])
    submit = SubmitField("Submit")


class RegistrationForm(FlaskForm):
    username =StringField('Username: ', validators=[DataRequired()])
    email = StringField('Email: ', validators=[DataRequired(),Email()])
    password= PasswordField('Password: ', validators=[DataRequired(), EqualTo('pass_confirm', message='Passwords must match!')])
    pass_confirm = PasswordField('Confirm Password: ', validators=[DataRequired()])
    submit = SubmitField("Log In")

    def check_email(self,field):
        if User.query.filter_by(email = field.data).first():
            raise ValidationError('Your email has been already registered!')

    def check_username(self,field):
        if User.query.filter_by(username = field.data).first():
            raise ValidationError('Username is already taken!')

class LoginForm(FlaskForm):
    email = StringField('Email: ', validators=[DataRequired(),Email()])
    password =  PasswordField("Password: ",  validators=[DataRequired()])
    submit = SubmitField("Log In")
