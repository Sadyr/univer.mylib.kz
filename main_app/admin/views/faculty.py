from flask import render_template, session, g , request, url_for, redirect

from main_app.admin import bp 
from main_app.auth import routes

# import from models
#from main_app.models.auth import user_login , get_user  
#from main_app.models.database import Session
from main_app.models.teacher import Teacher
from main_app.models.student import Student
from main_app.models.common import *

from sqlalchemy.orm.exc import NoResultFound
from sqlalchemy import and_, Select
from main_app.models.init_db import init_database,insert_main_data, insert_basic_data, insert_student, drob_db



@bp.route('/faculties')
@routes.login_required
def faculties():
    faculties = get_faculties()
    return render_template('admin/faculty/faculties.html', faculties=faculties)


@bp.route('/show_faculty/<int:faculty_id>')
@routes.login_required
def show_faculty(faculty_id):
    faculty_id = faculty_id
    specialities = get_specialities(faculty_id)
    faculty = get_faculty(faculty_id)
    return render_template('admin/faculty/faculty.html', faculty=faculty, specialities=specialities)


@bp.route('/delete_faculty/<int:faculty_id>')
@routes.login_required
def delete_faculty(faculty_id):
    with g.database as db:
        faculty = get_faculty(faculty_id)
        db.delete(faculty)
        db.commit()
    return redirect(url_for('admin.faculties'))

@bp.route('/add_faculty', methods=('GET', 'POST'))
@routes.login_required
def add_faculty():
    if request.method == 'POST':
        name = request.form['name']
        description = request.form['description']
        faculty = Faculty(name=name, description=description)
        add_object(faculty)
        return redirect(url_for('admin.faculties'))
    else:
        return render_template('admin/faculty/add_faculty.html')
    
@bp.route('/udpate_faculty/<int:faculty_id>', methods=('GET', 'POST'))
@routes.login_required
def update_faculty(faculty_id):
    if request.method == 'POST':
        with  g.database as db:
            faculty = db.query(Faculty).filter(Faculty.id==faculty_id).first()
            faculty.name = request.form['name']
            faculty.description = request.form['description']
            db.commit()
        return redirect(url_for('admin.show_faculty', faculty_id=faculty_id))
    else:
        faculty = get_faculty(faculty_id=faculty_id)
        return render_template('admin/faculty/update_faculty.html', faculty=faculty)

def add_object(object):
    with g.database as db:
            db.add(object)
            db.commit()

def get_faculties():
     with g.database  as db:
        faculties = db.query(Faculty).all()
        return faculties
     
def get_specialities(faculty_id):
     with g.database  as db:
        specialities = db.query(Speciality).filter(Speciality.faculty_id==faculty_id)
        return specialities
     
def get_faculty(faculty_id):
     with g.database  as db:
        stmt = Select(Faculty).filter(Faculty.id == faculty_id)
        try:
            faculty = db.scalars(stmt).one()
        except NoResultFound:
            faculty = 0
        return faculty