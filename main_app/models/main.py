from sqlalchemy import and_, Select
from main_app.models.student import Student
from main_app.models.common import Gender,College_group
from main_app.models.teacher import Teacher
from sqlalchemy.orm.exc import NoResultFound

from main_app.models.database import  Session
from init_db import init_database,insert_main_data, insert_basic_data, insert_student, drob_db


def is_student(email, password):
    email = email
    password = password
    stmt = Select(Student).filter(and_(Student.email == email, Student.password == password))
    try:
        student = session.scalars(stmt).one()
    except NoResultFound:
        student = 0
    return student

def is_worker(email, password):
    email = email
    password = password
    stmt = Select(Teacher).filter(and_(Teacher.email == email, Teacher.password == password))
    try:
        worker = session.scalars(stmt).one()
    except NoResultFound:
        worker = 0
    return worker

def which_user_group(person):
    if person.user_group_id == 1:
        print('Вы группе админа ')
    elif person.user_group_id == 2:
        print('Вы в группе работников')
    else:
        print('Вы в группе студентов')








def get_students():
    students = session.query(Student).all()
    for i in students:
            print(i)


if __name__== '__main__':
    drob_db()
    init_database()
    #insert_basic_data()
    insert_main_data()
    #insert_student()
   #with Session() as session:
        # query for individual columns
        #statement = Select(Student.firstname, Student.password, Student.email)

        # list of Row objects
        #rows = session.execute(statement).all()
        #print(type(rows[0][0])) 
        #print(rows)   
        #for u in session.query(Gender).all():
        #    print(u.name, u.id)
        #stmt = Select(College_group).where(College_group.speciality_id == 1)
        #result = session.execute(stmt)
        #for i in result.scalars():
           # print(i.id)   
"""
       # email = 'sadyr0012@gmail.com'
        password = '12345'
        student = is_student(email=email, password=password)
        if student == 0:
            worker = is_worker(email=email, password=password)
            if worker == 0:
                print("Введенные вами учетные данные некорретные. Проверьте еще раз")
            else:
                which_user_group(person=worker)
        else:
            which_user_group(person=student) """
        


        #student_email = Select(Student).where(Student.email == email)
        #worker_email = Select(Teacher).where(Teacher.email == email)
        #try:
        #    student = session.scalars(student_email).one()
        #except NoResultFound:
        #    student = 0
        #    print('Вы не являетесь студентом')
        #if student:
          #  print('Вы студент')
          #  student_pswd = Select(Student).where(Student.password == password)
          #  try:
           #     student = session.scalars(student_pswd).one()
           # except NoResultFound:
           #     student = 0
           #     print('Пароль студента неверный')
           # print('Пароль корректный. Редирект на страницу студента')
            
        #print(result.firstname)
        #print("hell")
        #result = session.scalars(user)
        #for i in result:
        #    print(i.name)
        


    


