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

@bp.route('/specialities/<int:faculty_id>')
@routes.login_required
def specialities(faculty_id):
    specialities = get_specialities(faculty_id)
    faculty = get_faculty(faculty_id)
    return render_template('admin/speciality/specialities.html', specialities=specialities, faculty=faculty)

def get_specialities(faculty_id):
     with g.database  as db:
        specialities = db.query(Speciality).filter(Speciality.faculty_id==faculty_id)
        return specialities
     
def get_faculty(faculty_id):
     with g.database  as db:
        faculty = db.query(Faculty).filter(Faculty.id==faculty_id).one()
        return faculty
       
def get_curriculums():
     with g.database  as db:
        curriculums = db.query(Curriculum).all()
        return curriculums
     
@bp.route('/add_speciality/<int:faculty_id>',methods=('GET', 'POST'))
@routes.login_required
def add_speciality(faculty_id):
    faculty = get_faculty(faculty_id)
    curriculums =  get_curriculums()
    if request.method == 'POST':
        name = request.form['name']
        description = request.form['description']
        code = request.form['code']
        faculty_id = faculty_id
        curriculum_id = request.form['curriculum_id']
        speciality = Speciality(name=name, description=description, faculty_id=faculty_id, curriculum_id=curriculum_id, code=code)
        add_object(speciality)
        return redirect(url_for('admin.specialities', faculty_id = faculty_id))
    else:
        return render_template('admin/speciality/add_speciality.html', curriculums=curriculums, faculty=faculty)


@bp.route('/show_speciality/<int:speciality_id>')
@routes.login_required
def show_speciality(speciality_id):
    return 'Данная страница в разработке'

@bp.route('/delete_speciality/<int:speciality_id>$<int:faculty_id>')
@routes.login_required
def delete_speciality(speciality_id,faculty_id ):
    with g.database as db:
        speciality = get_speciality(speciality_id)
        db.delete(speciality)
        db.commit()
    return redirect(url_for('admin.specialities', faculty_id=faculty_id))


def get_speciality(speciality_id):
     with g.database  as db:
        stmt = Select(Speciality).filter(Speciality.id == speciality_id)
        try:
            speciality = db.scalars(stmt).one()
        except NoResultFound:
            speciality = 0
        return speciality

@bp.route('/update_speciality/<int:speciality_id>$<int:faculty_id>',methods=('GET', 'POST') )
@routes.login_required
def update_speciality(speciality_id,faculty_id ):
   faculty = get_faculty(faculty_id=faculty_id)
   curriculums =  get_curriculums()
   if request.method == 'POST':
        with  g.database as db:
            speciality = db.query(Speciality).filter(Speciality.id==speciality_id).first()
            speciality.name = request.form['name']
            speciality.description = request.form['description']
            speciality.code = request.form['code']
            speciality.curriculum_id = request.form['curriculum_id']
            db.commit()
        return redirect(url_for('admin.specialities', faculty_id=faculty_id))
   else:
        speciality = get_speciality(speciality_id=speciality_id)
        return render_template('admin/speciality/update_speciality.html', speciality=speciality, faculty=faculty, curriculums=curriculums)
   
def add_object(object):
    with g.database as db:
            db.add(object)
            db.commit()