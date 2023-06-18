from flask import render_template, session, g , request, url_for, redirect

from main_app.admin import bp 
from main_app.auth import routes

# import from models
#from main_app.models.auth import user_login , get_user  
#from main_app.models.database import Session
from main_app.models.teacher import Teacher
from main_app.models.student import Student
from main_app.models.common import *
from main_app.models.course import *


from sqlalchemy.orm.exc import NoResultFound
from sqlalchemy import and_, Select
from main_app.models.init_db import init_database,insert_main_data, insert_basic_data, insert_student, drob_db

@bp.route('/students')
@routes.login_required
def students():
    students = get_students()
    return render_template('admin/student/students.html', students=students)



@bp.route('/show_student/<int:student_id>')
@routes.login_required
def show_student(student_id):
    student = get_student(student_id)
    portfolios = get_portfolios_by_student(student_id)
    return render_template('admin/student/student.html', student=student, portfolios=portfolios)


@bp.route('/add_student',  methods=('GET', 'POST'))
@routes.login_required
def add_student():
    college_groups = get_college_groups()
    if request.method == 'POST':
        firstname = request.form['firstname']
        lastname = request.form['lastname']
        middlename = request.form['middlename']
        birthday = request.form['birthday']
        bio = request.form['bio']
        picture = "https://placeimg.com/640/480/arch/any"
        gender_id = request.form['gender_id']
        email = request.form['email']
        phone = request.form['phone']
        password = request.form['password']
        user_group_id = 3
        college_group_id = request.form['college_group_id']
        student = Student (
            firstname = firstname,lastname = lastname, middlename = middlename,
            birthday = birthday, bio = bio, picture = picture,
            gender_id = gender_id, email = email, phone = phone,
            password=password, user_group_id = user_group_id,
            college_group_id = college_group_id )
        add_object(student)
        return redirect(url_for('admin.students'))
    else:
        return render_template('admin/student/add_student.html', college_groups=college_groups)


@bp.route('/update_student/<int:student_id>',  methods=('GET', 'POST'))
@routes.login_required
def update_student(student_id):
    college_groups = get_college_groups()
    if request.method == 'POST':
        with g.database as db:
            student = db.query(Student).filter(Student.id==student_id).first()
            student.firstname =  request.form['firstname']
            student.lastname = request.form['lastname']
            student.middlename = request.form['middlename']
            student.birthday = request.form['birthday']
            student.bio = request.form['bio']
            student.picture = "https://placeimg.com/640/480/arch/any"
            student.gender_id = request.form['gender_id']
            student.email = request.form['email']
            student.phone = request.form['phone']
            student.password = request.form['password']
            student.user_group_id = 3
            student.college_group_id = request.form['college_group_id']
            db.commit()
        return redirect(url_for('admin.show_student',student_id = student_id))
    
    else:
        student = get_student(student_id)
        return render_template('admin/student/update_student.html',student=student, college_groups=college_groups)


@bp.route('/delete_student/<int:student_id>')
@routes.login_required
def delete_student(student_id):
    with g.database as db:
        student = get_student(student_id)
        db.delete(student)
        db.commit()
    return redirect(url_for('admin.students'))
        

def add_object(object):
    with g.database as db:
            db.add(object)
            db.commit()


def get_students():
    with g.database  as db:
        students = db.query(Student).all()
    return students

def get_student(id):
    with g.database  as db:
        stmt = Select(Student).filter(Student.id == id)
        try:
            student = db.scalars(stmt).one()
        except NoResultFound:
            student = 0
    return student

def get_college_groups():
    with g.database  as db:
        groups = db.query(College_group).all()
    return groups

def get_genders():
    with g.database  as db:
        genders = db.query(Gender).all()
    return genders


@bp.route('/add_portfolio_by_student/<int:student_id>',  methods=('GET', 'POST'))
@routes.login_required
def add_portfolio_by_student(student_id):
    if request.method == 'POST':
        student_id = student_id
        name = request.form['name']
        description = request.form['description']
        field = request.form['field']
        resource = request.form['resource']
        data_of_start = request.form['data_of_start']
        data_of_end = request.form['data_of_end']
        portfolio = Portfolio (
           student_id=student_id,
             name=name,
             description=description,field=field,
             resource=resource, data_of_start=data_of_start,
            data_of_end=data_of_end)
        add_object(portfolio)
        return  redirect(url_for('admin.show_student',student_id = student_id))
    else:
        return render_template('admin/student/add_portfolio.html',student_id=student_id)

@bp.route('/update_portfolio_by_student/<int:portfolio_id>$<int:student_id>',  methods=('GET', 'POST'))
@routes.login_required
def update_portfolio_by_student(portfolio_id, student_id):
    if request.method == 'POST':
        with g.database as db:
            portfolio = db.query(Portfolio).filter(Portfolio.id==portfolio_id).first()
            portfolio.name = request.form['name']
            portfolio.description = request.form['description']
            portfolio.field = request.form['field']
            portfolio.resource = request.form['resource']
            portfolio.data_of_start = request.form['data_of_start']
            portfolio.data_of_end = request.form['data_of_end']
            db.commit()
        return redirect(url_for('admin.show_student',student_id = student_id))
    else:
        portfolio = get_portfolio(portfolio_id)
        return render_template('admin/student/update_portfolio.html',portfolio=portfolio )

def get_portfolio(portfolio_id):
    with g.database  as db:
        stmt = Select(Portfolio).filter(Portfolio.id == portfolio_id)
        try:
            portfolio = db.scalars(stmt).one()
        except NoResultFound:
            portfolio = 0
    return portfolio

def get_portfolios_by_student(student_id):
    with g.database  as db:
        stmt = Select(Portfolio).filter(Portfolio.student_id == student_id)
        try:
            portfolio = db.scalars(stmt).all()
        except NoResultFound:
            portfolio = 0
    return portfolio


@bp.route('/delete_portfolio_by_student/<int:portfolio_id>$<int:student_id>')
@routes.login_required
def delete_portfolio_by_student(portfolio_id, student_id):
    with g.database as db:
        portfolio = get_portfolio(portfolio_id)
        db.delete(portfolio)
        db.commit()
    return redirect(url_for('admin.show_student',student_id = student_id))
