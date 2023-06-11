from flask import ( flash, g, redirect,  render_template, request, session, url_for)
from main_app.auth import bp 
import functools

# import from models
#from main_app.models.auth import user_login , get_user  
from main_app.models.database import Session
from main_app.models.teacher import Teacher
from main_app.models.student import Student
from sqlalchemy.orm.exc import NoResultFound
from sqlalchemy import and_, Select
from main_app.models.init_db import init_database,insert_main_data, insert_basic_data, insert_student, drob_db



@bp.route('/login', methods = ('GET', 'POST'))
def login():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']
        user_data = user_login(email=email, password=password)
        if user_data != 0:
            session.clear() 
            return show_page(user_data=user_data)
        else:
            return "Incorrect login or password"
    return render_template('auth/login.html')

@bp.route('/logout', methods = ('GET', 'POST'))
def logout():
    return remove_user_from_session()


@bp.before_app_request
def load_user():
    user_id = session.get('user_id')
    user_group = session.get('user_group_id')
    if user_id is None:
        g.user = None
    else:
        if user_group == 1 or user_group == 3:
            user = get_user(user_id=user_id, user_object= Student)
            g.user = user
            g.database = Session()
        elif user_group == 2:
            user = get_user(user_id=user_id, user_object= Teacher)
            g.user = user
            g.database = Session
        

def add_user_in_session(user_data):
    session.clear()
    session['user_id'] = user_data.id
    session['user_group_id'] = user_data.user_group_id

def remove_user_from_session():
    session.clear()
    return redirect(url_for('auth.login'))


def show_page(user_data):
    print('run show page')
    user_data = user_data
    add_user_in_session(user_data=user_data)
    if session['user_group_id'] == 1: 
        return redirect(url_for('admin.index'))
    elif session['user_group_id'] == 2:
        return redirect(url_for('teacher.index'))
    else:
        return redirect(url_for('student.index'))


def login_required(view):
    @functools.wraps(view)
    def wrapped_view(**kwargs):
        if g.user is None:
            return redirect(url_for('auth.login'))
        return view(**kwargs)
    return wrapped_view

def user_login(email, password):
    email = email
    password = password
    student = is_student(email=email,password=password)
    if student == 0:
        worker = is_worker(email=email, password=password)
        if worker == 0:
            return 0
        else:
            return worker
    else:
        return student


def is_student(email, password):
    email = email
    password = password
    with Session() as session:
        stmt = Select(Student).filter(and_(Student.email == email, Student.password == password))
        try:
            student = session.scalars(stmt).one()
        except NoResultFound:
            student = 0
    return student

def is_worker(email, password):
    email = email
    password = password
    with Session() as session:
        stmt = Select(Teacher).filter(and_(Teacher.email == email, Teacher.password == password))
        try:
            worker = session.scalars(stmt).one()
        except NoResultFound:
            worker = 0
    return worker


def get_user(user_id, user_object):
    user_table = user_object
    with Session() as session:
        stmt = Select(user_table).filter(user_table.id == user_id)
        try:
            user = session.scalars(stmt).one()
        except NoResultFound:
            user = 0
    return user










            






""" @bp.route('/login', methods=('GET', 'POST'))
def login():
    if request.method == 'POST':
        login = request.form
        email = login['email']
        password = login['password']
        error = None
        user = Person.query.filter_by(email=email).first()      
        if user is None:
            error = 'Incorrect username.'
        elif  user.password != password:
            error = 'Incorrect password.'
        if error is None:
            session.clear()
            session['user_id'] = user.id
            session['person_group_id'] = user.person_group_id
            return user_group(person_group_id = int(session['person_group_id']))

    return render_template('auth/login.html')

            






"""
