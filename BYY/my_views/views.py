from flask import render_template,url_for,redirect,request,flash,Blueprint
from flask_login import login_user, login_required, logout_user
from BYY import db
from werkzeug.security import generate_password_hash, check_password_hash
from BYY.models import Book,Goal,Health,Blog, News, User
from BYY.my_views.forms import BookForm,HealthForm,GoalForm,BlogForm, NewsForm, LoginForm, RegistrationForm
from BYY.my_views.picture_handler import add_profile_pic, add_book_pic, makeHealthName, makePageName, makeBookName, add_progress_pic

my_views = Blueprint('my_views', __name__)

###########   Goal Views   ############s
@my_views.route('/goal/add_goal',methods=['GET','POST'])
@login_required
def add_goal():
    form = GoalForm()

    if form.validate_on_submit():

        goal = Goal(name = form.name.data,
                    area =form.area.data,
                    type =form.type.data,
                    description = form.description.data,
                    status= form.status.data,
                    update_news = form.update_news.data,
                    percent_complete=form.percent_complete.data)

        db.session.add(goal)
        db.session.commit()
        return redirect (url_for('my_views.goal_list'))
    return render_template('new_goal.html', form=form)

@my_views.route('/goal_list',methods=['GET','POST'])
@login_required
def goal_list():
    goals = Goal.query.all()
    return render_template('goal_list.html',goals=goals)

@my_views.route('/goal/<int:goal_id>/edit',methods=['GET','POST'])
@login_required
def edit_goal(goal_id):
    form=GoalForm()
    goal = Goal.query.get_or_404(goal_id)
    if form.validate_on_submit():

        goal.name = form.name.data
        goal.area = form.area.data
        goal.type = form.type.data
        goal.description = form.description.data
        goal.status = form.status.data
        goal.update_news = form.update_news.data
        goal.percent_complete = form.percent_complete.data

        db.session.commit()
        return redirect (url_for('my_views.goal_list'))
    elif request.method == 'GET':
        form.name.data = goal.name
        form.area.data = goal.area
        form.type.data = goal.type
        form.description.data = goal.description
        form.status.data = goal.status
        form.update_news.data = goal.update_news
        form.percent_complete.data = goal.percent_complete
    return render_template('edit_goal.html',form=form)

@my_views.route('/goal/<int:goal_id>/delete',methods=['GET','POST'])
@login_required
def delete_goal(goal_id):
    goal = Goal.query.get_or_404(goal_id)
    db.session.delete(goal)
    db.session.commit()

    flash('Goal Deleted')
    return redirect(url_for('my_views.goal_list'))

###########   Blog Views   ############
@my_views.route('/blog/add_blog',methods=['GET','POST'])
@login_required
def add_blog():
    form = BlogForm()

    if form.validate_on_submit():

        blog = Blog(subject = form.subject.data,
                    subtitle = form.subtitle.data,
                    cover_image = add_profile_pic(form.cover_image.data, makePageName(form.subject.data)),
                    blog_name = makePageName(form.subject.data),
                    text = form.text.data)

        db.session.add(blog)
        db.session.commit()
        return redirect (url_for('my_views.blog_list'))
    return render_template('new_blog.html', form=form)

@my_views.route('/blog/blog_list',methods=['GET','POST'])
@login_required
def blog_list():
    blogs = Blog.query.all()
    return render_template('blog_list.html',blogs=blogs)

@my_views.route('/blog/<int:blog_id>/edit',methods=['GET','POST'])
@login_required
def edit_blog(blog_id):
    blog = Blog.query.get_or_404(blog_id)
    form=BlogForm()

    if form.validate_on_submit():
        blog.subject = form.subject.data
        blog.text = form.text.data
        blog.subtitle = form.subtitle.data
        blog.cover_image = add_profile_pic(form.cover_image.data, makePageName(form.subject.data))
        blog.blog_name = makePageName(form.subject.data)

        db.session.commit()
        flash('Blog Post Updated')
        return redirect (url_for('my_views.blog_list'))
    elif request.method == 'GET':
        form.subject.data = blog.subject
        form.subtitle.data = blog.subtitle
        form.text.data = blog.text

    return render_template('edit_blog.html',form=form)

@my_views.route('/blog/<int:blog_id>/delete',methods=['GET','POST'])
@login_required
def delete_blog(blog_id):
    blog = Blog.query.get_or_404(blog_id)
    db.session.delete(blog)
    db.session.commit()

    flash('Blog Deleted')
    return redirect(url_for('my_views.blog_list'))
###########   Book Views   ############
@my_views.route('/book/add_book',methods=['GET','POST'])
@login_required
def add_book():
    form = BookForm()

    if form.validate_on_submit():
#title,author,pages,language,f_nf,genre,pub_date,review,cover_image,headline,book_name
        book = Book(title = form.title.data,
                    author = form.author.data,
                    pages = form.pages.data,
                    language = form.language.data,
                    f_nf = form.f_nf.data,
                    genre = form.genre.data,
                    pub_date = form.pub_date.data,
                    review = form.review.data,
                    cover_image = add_book_pic(form.cover_image.data, makeBookName(form.title.data)),
                    book_name = makeBookName(form.title.data),
                    headline = form.headline.data)

        db.session.add(book)
        db.session.commit()
        return redirect (url_for('my_views.book_list'))
    return render_template('new_book.html', form=form)

@my_views.route('/book/book_list',methods=['GET','POST'])
@login_required
def book_list():
    books = Book.query.all()
    return render_template('book_list.html',books=books)

@my_views.route('/book/<int:book_id>/edit',methods=['GET','POST'])
@login_required
def edit_book(book_id):
    #title,author,pages,f_nf,genre,pub_date,review,cover_image,headline
    form=BookForm()
    book = Book.query.get_or_404(book_id)
    if form.validate_on_submit():
        book.title = form.title.data
        book.author =form.author.data
        book.pages =form.pages.data
        book.f_nf = form.f_nf.data
        book.language = form.language.data
        book.genre = form.genre.data
        book.pub_date = form.pub_date.data
        book.review = form.review.data
        book.cover_image = add_book_pic(form.cover_image.data, makeBookName(form.title.data))
        book.headline = form.headline.data
        book.book_name = makeBookName(form.title.data)

        db.session.commit()
        return redirect (url_for('my_views.book_list'))
    elif request.method == 'GET':
        form.title.data = book.title
        form.author.data = book.author
        form.pages.data = book.pages
        form.language.data = book.language
        form.f_nf.data = book.f_nf
        form.genre.data = book.genre
        form.pub_date.data = book.pub_date
        form.review.data = book.review
        form.cover_image.data = book.cover_image
        form.headline.data = book.headline
    return render_template('edit_book.html',form=form)


@my_views.route('/book/<int:book_id>/delete',methods=['GET','POST'])
@login_required
def delete_book(book_id):
    book = Book.query.get_or_404(book_id)
    db.session.delete(book)
    db.session.commit()

    flash('Book Deleted')
    return redirect(url_for('my_views.book_list'))

##########   Health Views   ###########
@my_views.route('/health/add_health',methods=['GET','POST'])
@login_required
def add_health():
    form = HealthForm()

    if form.validate_on_submit():

        health = Health(weight = form.weight.data,
                    diastole =form.diastole.data,
                    systole =form.systole.data,
                    bicep = form.bicep.data,
                    chest = form.chest.data,
                    stomach = form.stomach.data,
                    waist = form.waist.data,
                    hips =form.hips.data,
                    health_name = makeHealthName(form.progress_image.data),
                    progress_image = add_progress_pic(form.progress_image.data, makeHealthName(form.progress_image.data)))

        db.session.add(health)
        db.session.commit()
        return redirect (url_for('my_views.health_list'))
    return render_template('new_health.html', form=form)

@my_views.route('/health/health_list',methods=['GET','POST'])
@login_required
def health_list():
    healths = Health.query.all()
    return render_template('health_list.html',healths=healths)

@my_views.route('/health/<int:health_id>/edit',methods=['GET','POST'])
@login_required
def edit_health(health_id):
    form=HealthForm()
    health = Health.query.get_or_404(health_id)
    if form.validate_on_submit():
        health.weight = form.weight.data
        health.diastole =form.diastole.data
        health.systole =form.systole.data
        health.bicep = form.bicep.data
        health.chest = form.chest.data
        health.stomach = form.stomach.data
        health.waist = form.waist.data
        health.hips = form.hips.data
        health.health_name = makeHealthName(form.progress_image.data)
        health.progress_image = add_progress_pic(form.progress_image.data, health_name)

        db.session.commit()
        return redirect (url_for('my_views.health_list'))
    elif request.method == 'GET':
            form.weight.data = health.weight
            form.diastole.data = health.diastole
            form.systole.data = health.systole
            form.bicep.data = health.bicep
            form.chest.data = health.chest
            form.stomach.data = health.stomach
            form.waist.data = health.waist
            form.hips.data = health.hips
            form.progress_image.data = health.progress_image
    return render_template('edit_health.html', form=form)

@my_views.route('/health/<int:health_id>/delete',methods=['GET','POST'])
@login_required
def delete_health(health_id):
    health = Health.query.get_or_404(health_id)
    db.session.delete(health)
    db.session.commit()

    flash('Health Deleted')
    return redirect(url_for('my_views.health_list'))

###########   News Views   ############
@my_views.route('/news/add_news',methods=['GET','POST'])
@login_required
def add_news():
    form = NewsForm()

    if form.validate_on_submit():

        news = News(area = form.area.data,
                    resolution = form.resolution.data,
                    subject = form.subject.data,
                    text = form.text.data)

        db.session.add(news)
        db.session.commit()
        return redirect (url_for('my_views.news_list'))
    return render_template('new_news.html', form=form)

@my_views.route('/news/news_list',methods=['GET','POST'])
@login_required
def news_list():
    newses = News.query.all()
    return render_template('news_list.html',newses=newses)

@my_views.route('/news/<int:news_id>/edit',methods=['GET','POST'])
@login_required
def edit_news(news_id):
    news = News.query.get_or_404(news_id)
    form=NewsForm()

    if form.validate_on_submit():
        news.area = form.area.data
        news.resolution = form.resolution.data
        news.subject = form.subject.data
        news.text = form.text.data

        db.session.commit()
        flash('News Post Updated')
        return redirect (url_for('my_views.news_list'))
    elif request.method == 'GET':
        form.area.data = news.area
        form.resolution.data = news.resolution
        form.subject.data = news.subject
        form.text.data = news.text
    return render_template('edit_news.html',form=form)

@my_views.route('/news/<int:news_id>/delete',methods=['GET','POST'])
@login_required
def delete_news(news_id):
    news = News.query.get_or_404(news_id)
    db.session.delete(news)
    db.session.commit()

    flash('News Deleted')
    return redirect(url_for('my_views.news_list'))


@my_views.route('/my_views_menu')
@login_required
def my_views_menu():
    return render_template('home.html')

@my_views.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('public_view.index'))

@my_views.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user.check_password(form.password.data) and user is not None:
            login_user(user)
            return redirect(url_for('my_views.my_views_menu'))
    return render_template("login.html", form= form)
