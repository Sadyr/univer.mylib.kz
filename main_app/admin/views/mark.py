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



@bp.route('/show_marks/<int:student_id>$<int:group_id>')
@routes.login_required
def show_marks(student_id, group_id):
    group_teachers_courses = get_group_teachers_courses(group_id)
    marks = get_marks_by_student(student_id)
    student=get_student(student_id)
    return render_template('admin/mark/marks.html',student=student, marks=marks, group_teachers_courses=group_teachers_courses, group_id=group_id)

def get_student(id):
    with g.database  as db:
        stmt = Select(Student).filter(Student.id == id)
        try:
            student = db.scalars(stmt).one()
        except NoResultFound:
            student = 0
    return student


def get_marks_by_student(student_id):
    with g.database  as db:
        stmt = Select(Mark).filter(Mark.student_id == student_id)
        try:
            marks = db.scalars(stmt).all()
        except NoResultFound:
            marks = 0
    return marks

def get_group_teachers_courses(group_id):
    with g.database  as db:
        group_teachers_courses = db.query(Group_teacher_course).filter(Group_teacher_course.college_group_id==group_id)
        return group_teachers_courses

@bp.route('/add_mark/<int:student_id>$<int:group_id>$<int:semester_id>$<int:course_id>$<int:teacher_course_id>$<int:teacher_id>', methods=('GET', 'POST'))
@routes.login_required
def add_mark(group_id,student_id, semester_id,course_id, teacher_course_id,teacher_id ):
    control_points = get_control_point()
    course = get_course(course_id)
    if request.method == 'POST':
        student_id=student_id
        college_group_id=group_id
        course_id=course_id
        teacher_id=teacher_id
        control_point_id=request.form['control_point_id']
        semester_id=semester_id
        mark=request.form['mark']
        teacher_course_id=teacher_course_id
        mark = Mark(
            student_id=student_id,college_group_id=college_group_id,
            course_id=course_id,teacher_id=teacher_id,
            control_point_id=control_point_id,semester_id=semester_id,
            mark=mark,teacher_course_id=teacher_course_id,
        )
        add_object(mark)
        return redirect(url_for('admin.show_marks', student_id=student_id, group_id=group_id))
    else:
        return render_template('admin/mark/add_mark.html',group_id=group_id,student_id=student_id, semester_id=semester_id,course=course, teacher_course_id=teacher_course_id,teacher_id=teacher_id, control_points=control_points)


@bp.route('/delete_mark/<int:mark_id>$<int:student_id>$<int:group_id>')
@routes.login_required
def delete_mark(mark_id, student_id, group_id):
    with g.database as db:
        mark = get_mark(mark_id)
        db.delete(mark)
        db.commit()
    return redirect(url_for('admin.show_marks', student_id=student_id, group_id=group_id))

def get_mark(mark_id):
    with g.database  as db:
            stmt = Select(Mark).filter(Mark.id == mark_id)
            try:
                mark = db.scalars(stmt).one()
            except NoResultFound:
                mark = 0
    return mark

@bp.route('/update_mark/<int:mark_id>$<int:student_id>$<int:group_id>', methods=('GET', 'POST'))
@routes.login_required
def update_mark(mark_id, group_id, student_id):
    if request.method == 'POST':
        with  g.database as db:
            mark = db.query(Mark).filter(Mark.id==mark_id).first()
            mark.mark=request.form['mark']
            mark.control_point_id=request.form['control_point_id']
            db.commit()
            return redirect(url_for('admin.show_marks',group_id=group_id, student_id=student_id ))
    else:
        mark = get_mark(mark_id)
        control_points = get_control_point()
        return render_template('admin/mark/update_mark.html',control_points=control_points ,mark=mark )



def get_course(course_id):
    with g.database  as db:
        stmt = Select(Course).filter(Course.id == course_id)
        try:
            course = db.scalars(stmt).one()
        except NoResultFound:
            course = 0
    return course



def get_control_point():
    with g.database  as db:
        control_points = db.query(Control_point).all()
        return control_points
    
def add_object(object):
    with g.database as db:
            db.add(object)
            db.commit()



def update_mark():
    pass

def delete_mark():
    pass