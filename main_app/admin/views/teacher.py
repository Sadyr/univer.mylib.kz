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

@bp.route('/teachers')
@routes.login_required
def teachers():
    teachers = get_teachers()
    return render_template('admin/teacher/teachers.html', teachers=teachers)

@bp.route('/show_teacher/<int:teacher_id>')
@routes.login_required
def show_teacher(teacher_id):
    teacher = get_teacher(teacher_id)
    teacher_courses = get_courses_by_teacher(teacher_id)
    portfolios = get_portfolios_by_teacher(teacher_id=teacher_id)
    return render_template('admin/teacher/teacher.html', teacher=teacher, teacher_courses=teacher_courses, portfolios=portfolios)


def get_teachers():
    with g.database  as db:
        teachers = db.query(Teacher).all()
    return teachers

@bp.route('/add_teacher',  methods=('GET', 'POST'))
@routes.login_required
def add_teacher():
    positions = get_positions()
    departments = get_departments()
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
        user_group_id = 2
        department_id = request.form['department_id']
        position_id = request.form['position_id']

        teacher = Teacher (
            firstname = firstname,lastname = lastname, middlename = middlename,
            birthday = birthday, bio = bio, picture = picture,
            gender_id = gender_id, email = email, phone = phone,
            password=password, user_group_id = user_group_id,
            department_id = department_id, position_id=position_id )
        add_object(teacher)
        return redirect(url_for('admin.teachers'))
    else:
        return render_template('admin/teacher/add_teacher.html', positions=positions,departments=departments )
    
@bp.route('/delete_teacher/<int:teacher_id>')
@routes.login_required
def delete_teacher(teacher_id):
    with g.database as db:
        teacher = get_teacher(teacher_id)
        db.delete(teacher)
        db.commit()
    return redirect(url_for('admin.teachers'))

def get_teacher(teacher_id):
    with g.database  as db:
        stmt = Select(Teacher).filter(Teacher.id == teacher_id)
        try:
            teacher = db.scalars(stmt).one()
        except NoResultFound:
            teacher = 0
    return teacher

def add_object(object):
    with g.database as db:
            db.add(object)
            db.commit()

def get_positions():
    with g.database  as db:
        positions = db.query(Position).all()
    return positions

def get_departments():
    with g.database  as db:
        departments = db.query(Department).all()
    return departments

@bp.route('/update_teacher/<int:teacher_id>',  methods=('GET', 'POST'))
@routes.login_required
def update_teacher(teacher_id):
    positions = get_positions()
    departments = get_departments()
    if request.method == 'POST':
        with g.database as db:
            teacher = db.query(Teacher).filter(Teacher.id==teacher_id).first()
            teacher.firstname =  request.form['firstname']
            teacher.lastname = request.form['lastname']
            teacher.middlename = request.form['middlename']
            teacher.birthday = request.form['birthday']
            teacher.bio = request.form['bio']
            teacher.picture = "https://placeimg.com/640/480/arch/any"
            teacher.gender_id = request.form['gender_id']
            teacher.email = request.form['email']
            teacher.phone = request.form['phone']
            teacher.password = request.form['password']
            teacher.user_group_id = 2
            teacher.department_id = request.form['department_id']
            teacher.position_id = request.form['position_id']

            db.commit()
        return redirect(url_for('admin.show_teacher',teacher_id = teacher_id))
    
    else:
        teacher = get_teacher(teacher_id)
        return render_template('admin/teacher/update_teacher.html',teacher=teacher, positions=positions,departments=departments )
    

def get_courses(department_id):
     with g.database  as db:
        courses = db.query(Course).filter(Course.department_id==department_id)
        return courses
     
def get_courses_by_teacher(teacher_id):
     with g.database  as db:
        teacher_courses = db.query(Teacher_course).filter(Teacher_course.teacher_id==teacher_id)
        return teacher_courses



@bp.route('/add_course_for_teacher/<int:teacher_id>',  methods=('GET', 'POST'))
@routes.login_required
def add_course_for_teacher(teacher_id):
    teacher = get_teacher(teacher_id)
    department_id = teacher.department_id
    courses = get_courses(department_id)
    if request.method == 'POST':
        course_id = request.form['course_id']
        teacher_id = teacher_id
        teacher_course = Teacher_course(course_id=course_id, teacher_id=teacher_id)
        add_object(teacher_course)
        return redirect(url_for('admin.show_teacher', teacher_id=teacher_id))
    else:
        return render_template('admin/teacher/add_course_for_teacher.html', courses=courses, teacher=teacher)

@bp.route('/delete_teacher_course/<int:teacher_course_id>')
@routes.login_required
def delete_teacher_course(teacher_course_id):
    with g.database as db:
        teacher_course = get_teacher_course(teacher_course_id)
        teacher_id = teacher_course.teacher.id
        db.delete(teacher_course)
        db.commit()
    return redirect(url_for('admin.show_teacher', teacher_id=teacher_id))

def get_teacher_course(teacher_course_id):
    with g.database  as db:
        stmt = Select(Teacher_course).filter(Teacher_course.id == teacher_course_id)
        try:
            teacher_course = db.scalars(stmt).one()
        except NoResultFound:
            teacher_course = 0
    return teacher_course

@bp.route('/show_schedule_by_teacher<int:teacher_id>$<int:semester_id>')
@routes.login_required
def show_schedule_by_teacher(teacher_id, semester_id):
    schedule = get_schedule_by_teacher(teacher_id,semester_id )
    teacher = get_teacher(teacher_id)
    return render_template('admin/schedule/schedule_for_teacher.html',schedule=schedule, teacher=teacher,  semester_id=semester_id)


def get_schedule_by_teacher(teacher_id, semester_id):
     with g.database  as db:
        #stmt = Select(Schedule).filter(and_(Schedule.teacher_course.cour == teacher_id, Schedule.semester_id == semester_id))
        try:
            #schedule = db.scalars(stmt).all()
            schedule = db.query(Schedule).join(Teacher_course).join(Teacher).filter(and_(Teacher.id == teacher_id, Schedule.semester_id == semester_id))
        except NoResultFound:
            schedule = 0
        return schedule
     
@bp.route('/add_portfolio/<int:teacher_id>',  methods=('GET', 'POST'))
@routes.login_required
def add_portfolio(teacher_id):
    if request.method == 'POST':
        teacher_id = teacher_id
        name = request.form['name']
        description = request.form['description']
        field = request.form['field']
        resource = request.form['resource']
        data_of_start = request.form['data_of_start']
        data_of_end = request.form['data_of_end']
        portfolio = Portfolio (
           teacher_id=teacher_id,
             name=name,
             description=description,field=field,
             resource=resource, data_of_start=data_of_start,
            data_of_end=data_of_end)
        add_object(portfolio)
        return  redirect(url_for('admin.show_teacher',teacher_id = teacher_id))
    else:
        return render_template('admin/teacher/add_portfolio.html',teacher_id=teacher_id)

@bp.route('/update_portfolio/<int:portfolio_id>$<int:teacher_id>',  methods=('GET', 'POST'))
@routes.login_required
def update_portfolio(portfolio_id, teacher_id):
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
        return redirect(url_for('admin.show_teacher',teacher_id = teacher_id))
    else:
        portfolio = get_portfolio(portfolio_id)
        return render_template('admin/teacher/update_portfolio.html',portfolio=portfolio )

def get_portfolio(portfolio_id):
    with g.database  as db:
        stmt = Select(Portfolio).filter(Portfolio.id == portfolio_id)
        try:
            portfolio = db.scalars(stmt).one()
        except NoResultFound:
            portfolio = 0
    return portfolio

def get_portfolios_by_teacher(teacher_id):
    with g.database  as db:
        stmt = Select(Portfolio).filter(Portfolio.teacher_id == teacher_id)
        try:
            portfolio = db.scalars(stmt).all()
        except NoResultFound:
            portfolio = 0
    return portfolio


@bp.route('/delete_portfolio/<int:portfolio_id>$<int:teacher_id>')
@routes.login_required
def delete_portfolio(portfolio_id, teacher_id):
    with g.database as db:
        portfolio = get_portfolio(portfolio_id)
        db.delete(portfolio)
        db.commit()
    return redirect(url_for('admin.show_teacher',teacher_id = teacher_id))
