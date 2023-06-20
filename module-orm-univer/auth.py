from sqlalchemy import and_, Select
from student import Student
from common import Gender,College_group
from teacher import Teacher
from sqlalchemy.orm.exc import NoResultFound
from database import  Session 

from .init_db import init_database,insert_main_data, insert_basic_data, insert_student, drob_db



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




def show_page(user_group):
    if user_group == 1:
        return 'admin'
    elif user_group == 2:
        return'worker'
    elif user_group == 3:
        return'student'
    else:
        return 'User Not Found'


def redirect():
    pass


if __name__=='__main__':
    email = 'ashs0012@gmail.co1m'
    password = '12345'
    with Session() as session:
        user_data = user_login(email=email, password=password)
        if user_data != 0:
            print(show_page(user_group=user_data.user_group_id))
            print(user_data)
        else:
            print(show_page(user_group=user_data))


