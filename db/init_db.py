import os
import psycopg2

conn = psycopg2.connect(
    host= os.environ('DATABASE_HOST'),
    database=os.environ('DATABASE_NAME'),
    user=os.environ['DB_USERNAME'],
    password=os.environ['DB_PASSWORD']
)

# Open a cursor to perform database operations
cur = conn.cursor()


# Execute a command: this creates a new table
# Table person
cur.execute('DROP TABLE IF EXISTS person cascade;')
cur.execute('CREATE TABLE person (id serial PRIMARY KEY,'
            'firstname varchar (150) NOT NULL,'
            'lastname varchar (150) NOT NULL,'
            'midlename varchar (150),'
            'birthday date NOT NULL,'
            'gender_id integer NOT NULL,'
            'email varchar (50) UNIQUE NOT NULL,'
            'password varchar (50) NOT NULL,'
            'phone_number varchar (50) NOT NULL,'
            'person_group_id integer NOT NULL,'
            'added date DEFAULT CURRENT_TIMESTAMP);')


# Table gender
cur.execute('DROP TABLE IF EXISTS gender;')
cur.execute('CREATE TABLE gender (id serial PRIMARY KEY,'
            'name varchar (50) UNIQUE NOT NULL);')

# Table person_group
cur.execute('DROP TABLE IF EXISTS person_group;')
cur.execute('CREATE TABLE person_group (id serial PRIMARY KEY,'
            'name varchar (50) UNIQUE NOT NULL,'
            'description text);')

# Table student
cur.execute('DROP TABLE IF EXISTS student;')
cur.execute('CREATE TABLE student (id serial PRIMARY KEY,'
            'person_id integer NOT NULL,'
            'college_group_id integer NOT NULL);')


# Table curriculum
cur.execute('DROP TABLE IF EXISTS curriculum cascade;')
cur.execute('CREATE TABLE curriculum (id serial PRIMARY KEY,'
            'name varchar (50)  NOT NULL,'
            'description text);')

# Table college_group
cur.execute('DROP TABLE IF EXISTS college_group cascade;')
cur.execute('CREATE TABLE college_group (id serial PRIMARY KEY,'
            'grade_id integer NOT NULL,'
            'curriculum_id integer NOT NULL,'
            'speciality_id integer NOT NULL);')

# Table grade
cur.execute('DROP TABLE IF EXISTS grade;')
cur.execute('CREATE TABLE grade (id serial PRIMARY KEY,'
            'number integer UNIQUE  NOT NULL);')


# Table speciality
cur.execute('DROP TABLE IF EXISTS speciality;')
cur.execute('CREATE TABLE speciality (id serial PRIMARY KEY,'
            'name varchar (120)  UNIQUE  NOT NULL,'
            'code varchar (120)  UNIQUE  NOT NULL,'
            'description text,'
            'faculty_id integer NOT NULL);')

# Table faculty
cur.execute('DROP TABLE IF EXISTS faculty cascade;')
cur.execute('CREATE TABLE faculty (id serial PRIMARY KEY,'
            'name varchar (120)  UNIQUE  NOT NULL,'
            'description text);')

# Table department
cur.execute('DROP TABLE IF EXISTS department cascade;')
cur.execute('CREATE TABLE department (id serial PRIMARY KEY,'
            'name varchar (120)  UNIQUE  NOT NULL,'
            'description text,'
            'faculty_id integer NOT NULL);')

# Table employee
cur.execute('DROP TABLE IF EXISTS employee cascade;')
cur.execute('CREATE TABLE employee (id serial PRIMARY KEY,'
            'person_id integer  NOT NULL,'
            'department_id integer NOT NULL,'
            'employee_position_id integer NOT NULL);')

# Table employee_position
cur.execute('DROP TABLE IF EXISTS employee_position;')
cur.execute('CREATE TABLE employee_position (id serial PRIMARY KEY,'
            'name varchar (120)  UNIQUE  NOT NULL,'
            'position_category_id integer NOT NULL);')

# Table position_category
cur.execute('DROP TABLE IF EXISTS position_category;')
cur.execute('CREATE TABLE position_category (id serial PRIMARY KEY,'
            'name varchar (120)  UNIQUE  NOT NULL);')

# Table course
cur.execute('DROP TABLE IF EXISTS course cascade;')
cur.execute('CREATE TABLE course (id serial PRIMARY KEY,'
            'name varchar (120)  UNIQUE  NOT NULL,'
            'short_name varchar (120) NOT NULL,'
            'description text NOT NULL ,'
            'course_credit integer NOT NULL,'
            'theoretical_hours integer NOT NULL,'
            'experiment_hours integer NOT NULL,'
            'department_id integer NOT NULL);')

# Table  course_teacher
cur.execute('DROP TABLE IF EXISTS  course_teacher cascade;')
cur.execute('CREATE TABLE  course_teacher (id serial PRIMARY KEY,'
            'employee_id integer  NOT NULL,'
            'course_id integer  NOT NULL);')


# Table schedule
cur.execute('DROP TABLE IF EXISTS schedule;')
cur.execute('CREATE TABLE schedule (id serial PRIMARY KEY,'
            'weekday_id integer NOT NULL,'
            'semester_id integer NOT NULL,'
            'control_point_id integer NOT NULL ,'
            'course_date date NOT NULL ,'
            'course_time_id integer NOT NULL,'
            'course_teacher_id integer NOT NULL,'
            'college_group_id integer NOT NULL,'
            'lesson_type_id integer NOT NULL,'
            'office varchar (30));')

# Table weekday
cur.execute('DROP TABLE IF EXISTS weekday;')
cur.execute('CREATE TABLE weekday (id serial PRIMARY KEY,'
            'name varchar (100) NOT NULL);')


# Table course_time
cur.execute('DROP TABLE IF EXISTS course_time;')
cur.execute('CREATE TABLE course_time (id serial PRIMARY KEY,'
            'name varchar (50) NOT NULL,'
            'start_time time,'
            'finish_time time);')

# Table lesson_type
cur.execute('DROP TABLE IF EXISTS lesson_type;')
cur.execute('CREATE TABLE lesson_type (id serial PRIMARY KEY,'
            'name varchar (100) NOT NULL);')

# Table semester
cur.execute('DROP TABLE IF EXISTS semester;')
cur.execute('CREATE TABLE semester (id serial PRIMARY KEY,'
            'name varchar (100) NOT NULL);')


# Table control_point
cur.execute('DROP TABLE IF EXISTS control_point;')
cur.execute('CREATE TABLE control_point (id serial PRIMARY KEY,'
            'name varchar (100) NOT NULL);')


# Foreignn  Key
cur.execute(
    'ALTER TABLE person ADD FOREIGN KEY (gender_id) REFERENCES gender (id);')
cur.execute(
    'ALTER TABLE person ADD FOREIGN KEY (person_group_id) REFERENCES person_group (id);')

cur.execute(
    'ALTER TABLE student ADD FOREIGN KEY (person_id) REFERENCES person (id) ON DELETE CASCADE;')
cur.execute(
    'ALTER TABLE student ADD FOREIGN KEY (college_group_id) REFERENCES college_group (id);')

cur.execute(
    'ALTER TABLE college_group ADD FOREIGN KEY (grade_id) REFERENCES grade (id);')
cur.execute(
    'ALTER TABLE college_group ADD FOREIGN KEY (curriculum_id) REFERENCES curriculum (id);')
cur.execute(
    'ALTER TABLE college_group ADD FOREIGN KEY (speciality_id) REFERENCES speciality (id);')

cur.execute(
    'ALTER TABLE speciality ADD FOREIGN KEY (faculty_id) REFERENCES faculty (id);')

cur.execute(
    'ALTER TABLE department ADD FOREIGN KEY (faculty_id) REFERENCES faculty (id);')

cur.execute(
    'ALTER TABLE employee ADD FOREIGN KEY (person_id) REFERENCES person (id) ON DELETE CASCADE;')
cur.execute(
    'ALTER TABLE employee ADD FOREIGN KEY (department_id) REFERENCES department (id);')
cur.execute(
    'ALTER TABLE employee ADD FOREIGN KEY (employee_position_id) REFERENCES employee_position (id);')

cur.execute('ALTER TABLE employee_position ADD FOREIGN KEY (position_category_id) REFERENCES position_category (id);')

cur.execute(
    'ALTER TABLE course ADD FOREIGN KEY (department_id) REFERENCES department (id);')

cur.execute(
    'ALTER TABLE course_teacher ADD FOREIGN KEY (employee_id) REFERENCES employee (id);')
cur.execute(
    'ALTER TABLE course_teacher ADD FOREIGN KEY (course_id) REFERENCES course (id);')

cur.execute(
    'ALTER TABLE schedule ADD FOREIGN KEY (semester_id) REFERENCES semester (id);')
cur.execute(
    'ALTER TABLE schedule ADD FOREIGN KEY (weekday_id) REFERENCES weekday (id);')
cur.execute(
    'ALTER TABLE schedule ADD FOREIGN KEY (control_point_id) REFERENCES control_point (id);')
cur.execute(
    'ALTER TABLE schedule ADD FOREIGN KEY (course_time_id) REFERENCES course_time (id);')
cur.execute(
    'ALTER TABLE schedule ADD FOREIGN KEY (course_teacher_id) REFERENCES course_teacher (id);')
cur.execute(
    'ALTER TABLE schedule ADD FOREIGN KEY (college_group_id) REFERENCES college_group (id);')
cur.execute(
    'ALTER TABLE schedule ADD FOREIGN KEY (lesson_type_id) REFERENCES lesson_type (id);')


# Insert data into the table

""" cur.execute('INSERT INTO gender (name)'
            'VALUES (%s)',
            ('Male',)
            )
cur.execute('INSERT INTO gender (name)'
            'VALUES (%s)',
            ('Female',))
cur.execute('INSERT INTO person_group (name, description)'
            'VALUES (%s, %s)',
            ('Admin','This is admin'))

cur.execute('INSERT INTO person_group (name, description)'
            'VALUES (%s, %s)',
            ('Worker','This is worker'))

cur.execute('INSERT INTO person_group (name, description)'
            'VALUES (%s, %s)',
            ('Student','This is student'))

cur.execute('INSERT INTO person (firstname, lastname, midlename, birthday, gender_id, email, password, phone_number,person_group_id )'
            'VALUES (%s, %s, %s, %s, %s, %s,%s, %s, %s)',
            ('Sadyr', 'Sauytov', 'Sabyrzhanuli','1997-08-27', 1,'sadyr0012@gmail.com','Nimeria_1227','87769842532','1')
           ) """

conn.commit()
cur.close()
conn.close()
