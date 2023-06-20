from common import  *
from student import *
from teacher import *
from course import *
from  database import Session, Base, engine
from sqlalchemy.sql import text


# Инициализация данных из файла data.sql
def insert_main_data():
    import os
    import psycopg2
    conn = psycopg2.connect(
        host='185.4.180.217',  #185.4.180.217  #localhost
        database='kaznudb',
        user='kaznuuser',
        password='Nimeria_1227')
    # Open a cursor to perform database operations
    cur = conn.cursor()
    with open('data.sql', 'r') as f:
        sql = f.read()
    cur.execute(sql)
    conn.commit()
    cur.close()
    conn.close()






def init_db():
    Base.metadata.create_all(engine)

def drob_db():
    Base.metadata.drop_all(engine)

# Создание таблиц на основе моделей
def init_database():
    init_db()
    print('--------------------')
    print('Таблицы успешно созданы')
    print('--------------------')


def insert_basic_data():
    session = Session()
    gender_1 = Gender(name = 'Муж')
    gender_2 = Gender(name = 'Жен')

    college_group_1 = College_group(name = 'ИС-1613', grade_id = 1)
    college_group_2 = College_group(name = 'БИО-2217',grade_id = 2 )
    college_group_3 = College_group(name = 'ФИП-1587',grade_id = 3 )
    college_group_4 = College_group(name = 'КТМО-1557',grade_id = 4 )
    

    user_group_1 = User_group(name = 'admin')
    user_group_2 = User_group(name = 'worker')
    user_group_3 = User_group(name = 'student')

    grade_1 = Grade(name = '1-Курс')
    grade_2 = Grade(name = '2-Курс')
    grade_3 = Grade(name = '3-Курс')
    grade_4 = Grade(name = '4-Курс')


    session.add_all([
        gender_1, gender_2,
        college_group_1, college_group_2,college_group_3, college_group_4,
        user_group_1, user_group_2, user_group_3,
        grade_1, grade_2, grade_3, grade_4,
    ])
    session.commit()
    print('--------------------')
    print('Базовые данные успешно добавлены')
    print('--------------------')

def insert_student():
    session = Session()
    student_a = Student(
    firstname = 'sadyr',lastname =  'sauytov',middlename = 'sabyrzhanuli',
    birthday= '27-08-1997', bio = 'This is my bio',
    picture = 'this is my picture',gender_id= 1,email = 'sad@sad.com',
    phone ='8777887788',password = 'mypassowrd',user_group_id= 1,college_group_id = 2,
     )
    student_b = Student(
    firstname = 'Mahs',lastname =  'Libre',middlename = 'Gulio',
    birthday= '27-08-1994', bio = 'This is my bio',
    picture = 'this is my picture',gender_id= 2,email = 'mahs@sad.com',
    phone ='877788774488',password = 'kmkrmfkrf',user_group_id= 2,college_group_id = 2,
     )
    session.add_all([student_a, student_b])
    session.commit()
    session.close()
    print('--------------------')
    print('Данные  студента успешно добавлены')
    print('--------------------')









