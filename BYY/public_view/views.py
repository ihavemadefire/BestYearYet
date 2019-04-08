from flask import render_template,Blueprint,url_for
from BYY.models import Blog, Health, News, Book, Goal
from datetime import date
from dateutil.relativedelta import relativedelta

public_view = Blueprint('public_view',__name__)


@public_view.route('/')
def index():
    contents = News.query.filter(News.date >= (date.today() - relativedelta(months=+1))).all()
    return render_template('index.html', contents = contents)

@public_view.route('/blog_posts')
def blog_posts():
    blog_posts = Blog.query.order_by(Blog.date.desc())
    return render_template('blog_posts.html',blog_posts=blog_posts)

@public_view.route('/blog_posts/<blog_name>')
def blog_post(blog_name):

    blog_post = Blog.query.filter_by(blog_name=blog_name).first()
    return render_template('blog_post.html', blog_post=blog_post)

@public_view.route('/books')
def books():
    books = Book.query.order_by(Book.date.desc())
    book_count = books.count()
    book_percent = book_count/75
    return render_template('books.html',books=books, book_count = book_count, book_percent = book_percent)

@public_view.route('/books/<book_name>')
def book(book_name):

    book = Book.query.filter_by(book_name=book_name).first()
    return render_template('book.html', title=book.title, date=book.date,
                            author=book.author, language=book.language, pages=book.pages, f_nf=book.f_nf,
                            genre=book.genre, pub_date=book.pub_date, review=book.review,
                            cover_image=book.cover_image, headline=book.headline, book_name=book.book_name)

@public_view.route('/resolutions')
def resolutions():

    areasa  = Goal.query.with_entities(Goal.area).distinct()
    areas = [i.area for i in areasa]

    nsy = Goal.query.filter_by(status='Not Yet Started').count()
    inf = Goal.query.filter_by(status='In Flight').count()
    cpt = Goal.query.filter_by(status='Online or Complete').count()
    healthc = Goal.query.filter_by(area='health').count()
    careerc = Goal.query.filter_by(area='career').count()
    homec = Goal.query.filter_by(area='home').count()
    projectsc = Goal.query.filter_by(area='projects').count()
    learningc = Goal.query.filter_by(area='learning').count()
    familyc = Goal.query.filter_by(area='family').count()
    headspacec = Goal.query.filter_by(area='headspace').count()


    return render_template('resolutions.html', areas=areas, nsy=nsy, inf=inf, cpt=cpt,
                            healthc=healthc, careerc=careerc, homec=homec, projectsc=projectsc,
                            learningc=learningc,familyc=familyc,headspacec=headspacec)

@public_view.route('/health',methods=['GET','POST'])
def health():

    healths = Health.query.all()
    first = healths[0]
    rest = healths[1:]
    return render_template('health.html', healths=healths, first=first, rest=rest)

@public_view.route('/about')
def about():
    return render_template('about.html')
