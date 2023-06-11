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


    

@bp.route('/courses')
@routes.login_required
def courses():
    courses = get_courses()
    return render_template('admin/course/courses.html', courses=courses)

@bp.route('/show_course/<int:course_id>')
@routes.login_required
def show_course(course_id):
    course = get_course(course_id)
    return render_template('admin/course/course.html', course=course)


@bp.route('/add_course', methods=('GET', 'POST'))
@routes.login_required
def add_course():
    if request.method == 'POST':
        name = request.form['name']
        shortname = request.form['shortname']
        credit_hours = request.form['credit_hours']
        theoretical_hours = request.form['theoretical_hours']
        experimental_hours = request.form['experimental_hours']
        description = request.form['description']
        department_id = request.form['department_id']
        course = Course(name=name,shortname=shortname, credit_hours=credit_hours, theoretical_hours=theoretical_hours,
                        experimental_hours=experimental_hours, description=description, department_id=department_id)
        add_object(course)
        return redirect(url_for('admin.courses'))
    else:
        departments = get_departments()
        return render_template('admin/course/add_course.html', departments=departments )

@bp.route('/delete_course/<int:course_id>')
@routes.login_required
def delete_course(course_id):
    with g.database as db:
        course = get_course(course_id)
        db.delete(course)
        db.commit()
    return redirect(url_for('admin.courses'))


@bp.route('/update_course/<int:course_id>',methods=('GET', 'POST') )
@routes.login_required
def update_course(course_id):
   if request.method == 'POST':
        with  g.database as db:
            course = db.query(Course).filter(Course.id==course_id).first()
            course.name = request.form['name']
            course.shortname = request.form['shortname']
            course.credit_hours = request.form['credit_hours']
            course.theoretical_hours = request.form['theoretical_hours']
            course.experimental_hours = request.form['experimental_hours']
            course.description = request.form['description']
            course.department_id = request.form['department_id']
            db.commit()
        return redirect(url_for('admin.courses'))
   else:
        course = get_course(course_id=course_id)
        departments = get_departments()
        return render_template('admin/course/update_course.html', course=course, departments=departments)



def get_departments():
     with g.database  as db:
        departments = db.query(Department).all()
        return departments

def add_object(object):
    with g.database as db:
            db.add(object)
            db.commit()

def get_course(course_id):
     with g.database  as db:
        stmt = Select(Course).filter(Course.id == course_id)
        try:
            course = db.scalars(stmt).one()
        except NoResultFound:
            course = 0
        return course

def get_courses():
     with g.database  as db:
        courses = db.query(Course).all()
        return courses
     

@bp.route('/add_teacher_course_to_group/<int:group_id>', methods=('GET', 'POST'))
@routes.login_required
def add_teacher_course_to_group(group_id):
    group = get_group(group_id)
    faculty_id = group.speciality.faculty_id 
    #teachers_courses = get_teachers_courses_by_faculty(faculty_id)
    teachers_courses=get_teachers_courses()
    if request.method == 'POST':
        teacher_course_id = request.form['teacher_course_id']
        college_group_id = group_id
        semester_id = request.form['semester_id']
        group_teacher_course = Group_teacher_course(teacher_course_id=teacher_course_id, college_group_id=college_group_id, semester_id=semester_id)
        add_object(group_teacher_course)
        return redirect(url_for('admin.show_group',group_id=group_id))
    else:
        semesters = get_semesters()
        return render_template('admin/course/add_teacher_course_to_group.html', teachers_courses=teachers_courses, group=group, semesters=semesters)

def get_semesters():
     with g.database  as db:
        semesters = db.query(Semester).all()
        return semesters    
   

def get_group(group_id):
     with g.database  as db:
        stmt = Select(College_group).filter(College_group.id == group_id)
        try:
            group = db.scalars(stmt).one()
        except NoResultFound:
            group = 0
        return group



def get_teachers_courses_by_faculty(faculty_id):
    with g.database  as db:
        teachers_courses = db.query(Teacher_course).join(Teacher).join(Department).filter(Department.faculty_id==faculty_id)
        return teachers_courses

def get_teachers_courses():
     with g.database  as db:
        teacher_courses = db.query(Teacher_course).all()
        return teacher_courses 
