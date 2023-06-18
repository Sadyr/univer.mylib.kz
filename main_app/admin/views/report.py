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


@bp.route('/report')
@routes.login_required
def report():
    students = get_students()
    semesters = get_semesters()
    return render_template('admin/mark/report.html', students=students, semesters=semesters)

def get_students():
    with g.database  as db:
        students = db.query(Student).all()
    return students

def get_semesters():
    with g.database  as db:
        semesters = db.query(Semester).all()
    return semesters

@bp.route('/get_report_by_semester/', methods=('GET', 'POST'))
@routes.login_required
def get_report_by_semester():
    if request.method == 'POST':
        student_id = request.form['student_id']
        semester_id = request.form['semester_id']
        student=get_student(student_id)
        group_teachers_courses = get_courses_by_semester(student.college_group_id, semester_id)
        marks=get_marks_by_semester(student_id, semester_id=semester_id)
        semester = get_semester(semester_id)
        total_mark_by_course,total_gpa_by_course  = total_mark_dict(marks=marks, group_teachers_courses=group_teachers_courses)
        return render_template('admin/mark/report_by_semester.html',total_gpa_by_course=total_gpa_by_course, total_mark_by_course=total_mark_by_course,semester=semester, marks=marks, student=student, group_teachers_courses=group_teachers_courses)



def total_mark_dict(group_teachers_courses, marks):
    sum = 0
    course_mark_dict = {}
    course_gpa_dict = {}

    leng = 0
    for group_teacher_course in group_teachers_courses:
        for mark in marks:
            if group_teacher_course.teacher_course.course_id == mark.course_id:
                sum=sum+mark.mark
                leng = leng + 1
        course_mark_dict[group_teacher_course.teacher_course.course.name] = (int(sum / leng) * group_teacher_course.teacher_course.course.credit_hours) / group_teacher_course.teacher_course.course.credit_hours
        course_gpa_dict[group_teacher_course.teacher_course.course.name] = get_gpa(int(sum / leng))
        sum = 0
        leng=0
    return (course_mark_dict, course_gpa_dict)







def  get_courses_by_semester(group_id, semester_id):
    with g.database  as db:
        stmt = Select(Group_teacher_course).filter(Group_teacher_course.semester_id == semester_id, Group_teacher_course.college_group_id==group_id)
        try:
            courses = db.scalars(stmt).all()
        except NoResultFound:
            courses = 0
    return courses

def get_student(student_id):
    with g.database  as db:
            stmt = Select(Student).filter(Student.id == student_id)
            try:
                student = db.scalars(stmt).one()
            except NoResultFound:
                student = 0
    return student

def get_semester(semester_id):
    with g.database  as db:
            stmt = Select(Semester).filter(Semester.id == semester_id)
            try:
                semester = db.scalars(stmt).one()
            except NoResultFound:
                semester = 0
    return semester

def get_course(course_id):
    with g.database  as db:
            stmt = Select(Course).filter(Course.id == course_id)
            try:
                course = db.scalars(stmt).one()
            except NoResultFound:
                course = 0
    return course




def get_mark(mark_id):
    with g.database  as db:
            stmt = Select(Mark).filter(Mark.id == mark_id)
            try:
                mark = db.scalars(stmt).one()
            except NoResultFound:
                mark = 0
    return mark

def get_marks_by_semester(student_id, semester_id):
    with g.database  as db:
        stmt = Select(Mark).filter(Mark.student_id == student_id, Mark.semester_id==semester_id)
        try:
            marks = db.scalars(stmt).all()
        except NoResultFound:
            marks = 0
    return marks

def get_marks_by_student(student_id):
    with g.database  as db:
        stmt = Select(Mark).filter(Mark.student_id == student_id, Mark.course_id==1, Mark.semester_id==1)
        try:
            marks = db.scalars(stmt).all()
        except NoResultFound:
            marks = 0
    return marks


def get_gpa(number):
    if number >= 95 and number <= 100:
        return 4
    elif number >= 90 and number <= 94:
        return 3.67
    elif number >= 85 and number <= 89:
        return 3.33
    elif number >= 80 and number <= 84:
        return 3
    elif number >= 75 and number <= 79:
        return 2.67
    elif number >= 70 and number <= 74:
        return 2.33
    elif number >= 65 and number <= 69:
        return 2
    elif number >= 60 and number <= 64:
        return 1.67
    elif number >= 55 and number <= 59:
        return 1.33
    elif number >= 50 and number <= 54:
        return 1
    elif number >= 0 and number <= 49:
        return 0


def get_report_by_group(group_id):
    pass
    #student:result_mark: result_gpa
    # result_mark = course_result_mark