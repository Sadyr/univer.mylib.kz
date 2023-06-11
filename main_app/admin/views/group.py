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
from main_app.models.init_db import init_database,insert_main_data, insert_basic_data, insert_student, drob_db, insert_student, drob_db


@bp.route('/show_group/<int:group_id>')
@routes.login_required
def show_group(group_id):
    students = get_students(group_id=group_id)
    group = get_group(group_id)
    group_teachers_courses = get_group_teachers_courses(group_id)
    return render_template('admin/group/group.html', group=group, students=students, group_teachers_courses=group_teachers_courses)

def get_students(group_id):
     with g.database  as db:
        students = db.query(Student).filter(Student.college_group_id ==group_id)
        return students

def get_group_teachers_courses(group_id):
    with g.database  as db:
        group_teachers_courses = db.query(Group_teacher_course).filter(Group_teacher_course.college_group_id==group_id)
        return group_teachers_courses


@bp.route('/delete_group_teacher_course/<int:group_teacher_course_id>$<int:group_id>')
@routes.login_required
def delete_group_teacher_course(group_teacher_course_id, group_id):
    with g.database as db:
        group_teacher_course = get_group_teacher_course(group_teacher_course_id)
        db.delete(group_teacher_course)
        db.commit()
    return redirect(url_for('admin.show_group', group_id=group_id))

def get_group_teacher_course(group_teacher_course_id):
    with g.database  as db:
        stmt = Select(Group_teacher_course).filter(Group_teacher_course.id == group_teacher_course_id)
        try:
            group_teacher_course = db.scalars(stmt).one()
        except NoResultFound:
            group_teacher_course = 0
    return group_teacher_course



def get_group(group_id):
    with g.database  as db:
        stmt = Select(College_group).filter(College_group.id == group_id)
        try:
            group = db.scalars(stmt).one()
        except NoResultFound:
            group = 0
    return group

@bp.route('/groups/')
@routes.login_required
def groups():
    groups = get_groups()
    return render_template('admin/group/groups.html', groups=groups)

def get_groups():
     with g.database  as db:
        groups = db.query(College_group).all()
        return groups
    
@bp.route('/delete_group/<int:group_id>')
@routes.login_required
def delete_group(group_id):
    with g.database as db:
        group = get_group(group_id)
        db.delete(group)
        db.commit()
    return redirect(url_for('admin.groups'))

def get_group(group_id):
     with g.database  as db:
        stmt = Select(College_group).filter(College_group.id == group_id)
        try:
            group = db.scalars(stmt).one()
        except NoResultFound:
            group = 0
        return group
     

@bp.route('/add_group', methods=('GET', 'POST'))
@routes.login_required
def add_group():
    specialities = get_specialities()
    grades = get_grades()
    if request.method == 'POST':
        name = request.form['name']
        grade_id = request.form['grade_id']
        speciality_id = request.form['speciality_id']
        group = College_group(name=name, grade_id=grade_id,speciality_id=speciality_id )
        add_object(group)
        return redirect(url_for('admin.groups'))
    else:
        return render_template('admin/group/add_group.html', specialities=specialities,grades=grades )
    
def get_grades():
     with g.database  as db:
        grades = db.query(Grade).all()
        return grades
     
def get_specialities():
     with g.database  as db:
        specialities = db.query(Speciality).all()
        return specialities
    
def add_object(object):
    with g.database as db:
            db.add(object)
            db.commit()

@bp.route('/update_group/<int:group_id>', methods=('GET', 'POST'))
@routes.login_required
def update_group(group_id):
    specialities = get_specialities()
    grades = get_grades()
    if request.method == 'POST':
        with  g.database as db:
            group = db.query(College_group).filter(College_group.id==group_id).first()
            group.name = request.form['name']
            group.grade_id = request.form['grade_id']
            group.speciality_id = request.form['speciality_id']
            db.commit()
        return redirect(url_for('admin.groups',group_id=group_id))
    else:
        group = get_group(group_id=group_id)
        return render_template('admin/group/update_group.html', group=group, grades=grades,specialities=specialities )
    

@bp.route('/show_schedule<int:group_id>$<int:semester_id>')
@routes.login_required
def show_schedule(group_id, semester_id):
     schedule = get_schedule_by_group(group_id, semester_id)
     group = get_group(group_id)

     return render_template('admin/schedule/schedule.html',schedule=schedule, group=group,  semester_id=semester_id)
     
     
def get_schedule_by_group(group_id, semester_id):
     with g.database  as db:
        stmt = Select(Schedule).filter(and_(Schedule.college_group_id == group_id, Schedule.semester_id == semester_id))
        try:
            schedule = db.scalars(stmt).all()
        except NoResultFound:
            schedule = 0
        return schedule
     

@bp.route('/add_schedule_by_group/<int:group_id>$<int:semester_id>', methods=('GET', 'POST'))
@routes.login_required
def add_schedule_by_group(group_id,semester_id):
    teachers_courses = get_teachers_courses(group_id, semester_id)
    day_of_week = get_day_of_week()
    lesson_time = get_lesson_time()
    lesson_type = get_lesson_type()
    if request.method == 'POST':
        teacher_course_id = request.form['teacher_course_id']
        college_group_id = group_id
        semester_id = semester_id
        day_of_week_id = request.form['day_of_week_id']
        lesson_time_id = request.form['lesson_time_id']
        lesson_type_id = request.form['lesson_type_id']
        room = request.form['room']

        schedule = Schedule(teacher_course_id=teacher_course_id,college_group_id=college_group_id,semester_id=semester_id, day_of_week_id=day_of_week_id, lesson_time_id=lesson_time_id, lesson_type_id=lesson_type_id, room=room )
        add_object(schedule)
        return redirect(url_for('admin.show_schedule',group_id=group_id, semester_id=semester_id ))
    else:
        return render_template('admin/schedule/add_schedule_by_group.html',teachers_courses=teachers_courses, day_of_week=day_of_week, lesson_time=lesson_time, lesson_type=lesson_type )

@bp.route('/delete_schedule/<int:schedule_id>$<int:group_id>$<int:semester_id>', methods=('GET', 'POST'))
@routes.login_required
def delete_schedule(schedule_id,group_id, semester_id ):
    with g.database as db:
        schedule = get_schedule(schedule_id)
        db.delete(schedule)
        db.commit()
    return redirect(url_for('admin.show_schedule',group_id=group_id, semester_id=semester_id ))



@bp.route('/update_schedule/<int:schedule_id>$<int:group_id>$<int:semester_id>', methods=('GET', 'POST'))
@routes.login_required
def update_schedule(schedule_id, group_id, semester_id):
    if request.method == 'POST':
        with  g.database as db:
            schedule = db.query(Schedule).filter(Schedule.id==schedule_id).first()
            schedule.teacher_course_id=request.form['teacher_course_id']
            schedule.college_group_id=group_id
            schedule.semester_id=semester_id
            schedule.day_of_week_id=request.form['day_of_week_id']
            schedule.lesson_time_id=request.form['lesson_time_id']
            schedule.lesson_type_id=request.form['lesson_type_id']
            schedule.room=request.form['room']
            db.commit()
            return redirect(url_for('admin.show_schedule',group_id=group_id, semester_id=semester_id ))
    else:
        schedule = get_schedule(schedule_id)
        teachers_courses = get_teachers_courses(group_id, semester_id)
        day_of_week = get_day_of_week()
        lesson_time = get_lesson_time()
        lesson_type = get_lesson_type()
        return render_template('admin/schedule/update_schedule.html',schedule=schedule ,teachers_courses=teachers_courses, day_of_week=day_of_week, lesson_time=lesson_time, lesson_type=lesson_type )

def get_schedule(schedule_id):
    with g.database  as db:
        stmt = Select(Schedule).filter(Schedule.id == schedule_id)
        try:
            schedule = db.scalars(stmt).one()
        except NoResultFound:
            schedule = 0
        return schedule
     


def get_day_of_week():
    with g.database  as db:
        day_of_week = db.query(Day_of_week).all()
        return day_of_week

def get_lesson_time():
    with g.database  as db:
        lesson_time = db.query(Lesson_time).all()
        return lesson_time

def get_lesson_type():
    with g.database  as db:
        lesson_type = db.query(Lesson_type).all()
        return lesson_type

def get_teachers_courses(group_id, semester_id):
    with g.database  as db:
        stmt = Select(Group_teacher_course).filter(and_(Group_teacher_course.college_group_id == group_id, Group_teacher_course.semester_id == semester_id))
        try:
            teachers_courses = db.scalars(stmt).all()
        except NoResultFound:
            teachers_courses = 0
        return teachers_courses

