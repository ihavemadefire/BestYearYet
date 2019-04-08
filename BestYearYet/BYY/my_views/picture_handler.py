import os
from PIL import Image
from flask import url_for,current_app



def makePageName(title):
    a = title.split()
    b = [i for i in a]
    e=[]
    for i in b:
        c = "".join([y.lower() for y in i if y.isalpha()])
        f= e.append(c)
    seperator = "-"
    g = seperator.join(e)
    page_name = g

    return (page_name)

def makeBookName(title):
    a = title.split()
    b = [i for i in a]
    e=[]
    for i in b:
        c = "".join([y.lower() for y in i if y.isalpha()])
        f= e.append(c)
    seperator = "-"
    g = seperator.join(e)
    book_name=g
    return (book_name)

def makeHealthName(title):
    seperator = "-"
    bounce = title.filename
    a = bounce.split()
    b = [i for i in a]
    e=[]
    for i in b:
        c = "".join([y.lower() for y in i if y.isalpha()])
        f= e.append(c)
    seperator = "-"
    g = seperator.join(e)
    health_name =g
    return (health_name)

def add_profile_pic(pic_upload,blog_title):


    filename = pic_upload.filename

    ext_type = filename.split('.')[-1]
    storage_filename = str(blog_title)+'.'+ext_type

    filepath = os.path.join(current_app.root_path, 'static\\blog_post_pics', storage_filename)

    pic = Image.open(pic_upload)
    pic.save(filepath)
    return storage_filename

def add_book_pic(pic_upload,book_title):

    filename = pic_upload.filename

    ext_type = filename.split('.')[-1]
    storage_filename = str(book_title)+'.'+ext_type

    filepath = os.path.join(current_app.root_path, 'static\\book_pics', storage_filename)

    pic = Image.open(pic_upload)
    pic.save(filepath)
    return storage_filename

def add_progress_pic(pic_upload,health_id):


        filename = pic_upload.filename

        ext_type = filename.split('.')[-1]
        storage_filename = str(health_id)+'.'+ext_type

        filepath = os.path.join(current_app.root_path, 'static\\progress_pics', storage_filename)

        pic = Image.open(pic_upload)
        pic.save(filepath)
        return storage_filename
