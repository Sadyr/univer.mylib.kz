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
from main_app.models.init_db import init_database,insert_main_data, insert_basic_data, insert_student, drob_db, insert_student, drob_db

@bp.route('/departments/<int:faculty_id>')
@routes.login_required
def departments(faculty_id):
    departments = get_departments(faculty_id)
    faculty = get_faculty(faculty_id)
    return render_template('admin/department/departments.html', departments=departments, faculty=faculty)

def get_departments(faculty_id):
     with g.database  as db:
        departments = db.query(Department).filter(Department.faculty_id==faculty_id)
        return departments
     
def get_faculty(faculty_id):
     with g.database  as db:
        faculty = db.query(Faculty).filter(Faculty.id==faculty_id).one()
        return faculty
     
@bp.route('/add_department/<int:faculty_id>',methods=('GET', 'POST'))
@routes.login_required
def add_department(faculty_id):
    faculty = get_faculty(faculty_id)
    if request.method == 'POST':
        name = request.form['name']
        description = request.form['description']
        faculty_id = faculty_id
        department = Department(name=name, description=description, faculty_id=faculty_id)
        add_object(department)
        return redirect(url_for('admin.departments', faculty_id = faculty_id))
    else:
        return render_template('admin/department/add_department.html',  faculty=faculty)
    
def add_object(object):
    with g.database as db:
            db.add(object)
            db.commit()

@bp.route('/delete_department/<int:department_id>$<int:faculty_id>')
@routes.login_required
def delete_department(department_id,faculty_id ):
    with g.database as db:
        department = get_department(department_id)
        db.delete(department)
        db.commit()
    return redirect(url_for('admin.departments', faculty_id=faculty_id))

def get_department(department_id):
     with g.database  as db:
        stmt = Select(Department).filter(Department.id == department_id)
        try:
            department = db.scalars(stmt).one()
        except NoResultFound:
            department = 0
        return department
     
@bp.route('/update_department/<int:department_id>$<int:faculty_id>',methods=('GET', 'POST') )
@routes.login_required
def update_department(department_id,faculty_id ):
   faculty = get_faculty(faculty_id=faculty_id)
   if request.method == 'POST':
        with  g.database as db:
            department = db.query(Department).filter(Department.id==department_id).first()
            department.name = request.form['name']
            department.description = request.form['description']
            db.commit()
        return redirect(url_for('admin.departments', faculty_id=faculty_id))
   else:
        department = get_department(department_id=department_id)
        return render_template('admin/department/update_department.html', department=department, faculty=faculty)
   
@bp.route('/show_department/<int:department_id>')
@routes.login_required
def show_department(department_id):
    return 'Данная страница в разработке'