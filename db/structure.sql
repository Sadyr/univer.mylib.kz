
-- CREATE TYPE gender AS ENUM ('Муж', 'Жен');
--DROP TYPE  IF EXISTS gender_enum cascade;
--CREATE TYPE gender_enum AS ENUM ('Муж', 'Жен');





--Create table person
DROP TABLE IF EXISTS person cascade;
CREATE TABLE person (id serial PRIMARY KEY,
firstname varchar (150) NOT NULL,
lastname varchar (150) NOT NULL,
midlename varchar (150),
birthday date NOT NULL,
gender_id integer NOT NULL,
email varchar (50) UNIQUE NOT NULL,
password varchar (50) NOT NULL,
phone_number varchar (50) NOT NULL,
person_group_id integer NOT NULL,
added date DEFAULT CURRENT_TIMESTAMP);

--Create table gender
DROP TABLE IF EXISTS gender;
CREATE TABLE gender (id serial PRIMARY KEY,
name varchar (50) UNIQUE NOT NULL);

-- Create table person_group
DROP TABLE IF EXISTS person_group;
CREATE TABLE person_group (id serial PRIMARY KEY,
name varchar (50) UNIQUE NOT NULL,
description text);

-- Create table student
DROP TABLE IF EXISTS student;
CREATE TABLE student (id serial PRIMARY KEY,
person_id integer NOT NULL,
college_group_id integer NOT NULL);


-- Create table curriculum
DROP TABLE IF EXISTS curriculum cascade;
CREATE TABLE curriculum (id serial PRIMARY KEY,
name varchar (50)  NOT NULL,
description text);

-- Create table college_group
DROP TABLE IF EXISTS college_group cascade;
CREATE TABLE college_group (id serial PRIMARY KEY,
name varchar(50) UNIQUE NOT NULL,
grade_id integer NOT NULL,
speciality_id integer NOT NULL);

-- Create table grade
DROP TABLE IF EXISTS grade;
CREATE TABLE grade (id serial PRIMARY KEY,
number integer UNIQUE  NOT NULL);

-- Create table speciality
DROP TABLE IF EXISTS speciality;
CREATE TABLE speciality (id serial PRIMARY KEY,
name varchar (120)    NOT NULL,
code varchar (120)  UNIQUE  NOT NULL,
curriculum_id integer NOT NULL, 
description text,
faculty_id integer NOT NULL);

-- Creat table faculty
DROP TABLE IF EXISTS faculty cascade;
CREATE TABLE faculty (id serial PRIMARY KEY,
name varchar (120)  UNIQUE  NOT NULL,
description text);

--Create table department
DROP TABLE IF EXISTS department cascade;
CREATE TABLE department (id serial PRIMARY KEY,
name varchar (120)  UNIQUE  NOT NULL,
description text,
faculty_id integer NOT NULL);

-- Create table employee
DROP TABLE IF EXISTS employee cascade;
CREATE TABLE employee (id serial PRIMARY KEY,
person_id integer  NOT NULL,
department_id integer NOT NULL,
employee_position_id integer NOT NULL);


-- Create table employee_position
DROP TABLE IF EXISTS employee_position;
CREATE TABLE employee_position (id serial PRIMARY KEY,
name varchar (120)  UNIQUE  NOT NULL,
position_category_id integer NOT NULL);

-- Create table position_category
DROP TABLE IF EXISTS position_category;
CREATE TABLE position_category (id serial PRIMARY KEY,
name varchar (120)  UNIQUE  NOT NULL);

--Create table teacher
DROP TABLE IF EXISTS teacher;
CREATE TABLE teacher (id serial PRIMARY KEY,
employee_id integer NOT NULL);




--Create table course
DROP TABLE IF EXISTS course cascade;
CREATE TABLE course (id serial PRIMARY KEY,
name varchar (120)  UNIQUE  NOT NULL,
short_name varchar (120) NOT NULL, -- 
description text NOT NULL ,
credit_hours integer NOT NULL,
theoretical_hours integer NOT NULL,
experiment_hours integer NOT NULL,
department_id integer NOT NULL);



-- Create table course_teacher
DROP TABLE IF EXISTS  course_teacher cascade;
CREATE TABLE  course_teacher (id serial PRIMARY KEY,
teacher_id integer  NOT NULL,
course_id integer  NOT NULL);

-- Create table schedule
DROP TABLE IF EXISTS schedule;
CREATE TABLE schedule (id serial PRIMARY KEY,
course_teacher_id integer NOT NULL,
college_group_id integer NOT NULL,
semester_id integer NOT NULL,
control_point_id integer NOT NULL ,
day_of_week_id integer NOT NULL,
course_date date NOT NULL ,
course_time_id integer NOT NULL,
lesson_type_id integer NOT NULL,
room_number varchar (30));

-- Create student_mark
DROP TABLE IF EXISTS student_mark;
CREATE TABLE student_mark (id serial PRIMARY KEY,
schedule_id integer NOT NULL,
student_id integer NOT NULL,
score integer NOT NULL,
control_type_id integer NOT NULL);

-- Create table control_type
DROP TABLE IF EXISTS control_type;
CREATE TABLE control_type (id serial PRIMARY KEY,
name varchar (100) NOT NULL);--current control, landmark control,inspection control




-- Create table day_of_week
DROP TABLE IF EXISTS day_of_week;
CREATE TABLE day_of_week (id serial PRIMARY KEY,
name varchar (100) NOT NULL);

-- Create table course_time
DROP TABLE IF EXISTS course_time;
CREATE TABLE course_time (id serial PRIMARY KEY,
name varchar (50) NOT NULL,
start_time time,
finish_time time);

-- Create table lesson_type
DROP TABLE IF EXISTS lesson_type;
CREATE TABLE lesson_type (id serial PRIMARY KEY,
name varchar (100) NOT NULL);

-- Create table semester
DROP TABLE IF EXISTS semester;
CREATE TABLE semester (id serial PRIMARY KEY,
name varchar (100) NOT NULL,
start_date DATE NOT NULL,
end_date DATE NOT NULL);

-- Create table control_point
DROP TABLE IF EXISTS control_point;
CREATE TABLE control_point (id serial PRIMARY KEY,
name varchar (100) NOT NULL);

-- Foreignn  Key
ALTER TABLE person ADD FOREIGN KEY (gender_id) REFERENCES gender (id);
ALTER TABLE person ADD FOREIGN KEY (person_group_id) REFERENCES person_group (id);

ALTER TABLE student ADD FOREIGN KEY (person_id) REFERENCES person (id) ON DELETE CASCADE;
ALTER TABLE student ADD FOREIGN KEY (college_group_id) REFERENCES college_group (id);

ALTER TABLE college_group ADD FOREIGN KEY (grade_id) REFERENCES grade (id);
ALTER TABLE college_group ADD FOREIGN KEY (speciality_id) REFERENCES speciality (id);

ALTER TABLE speciality ADD FOREIGN KEY (curriculum_id) REFERENCES curriculum (id);
ALTER TABLE speciality ADD FOREIGN KEY (faculty_id) REFERENCES faculty (id);

ALTER TABLE department ADD FOREIGN KEY (faculty_id) REFERENCES faculty (id);

ALTER TABLE employee ADD FOREIGN KEY (person_id) REFERENCES person (id) ON DELETE CASCADE;
ALTER TABLE employee ADD FOREIGN KEY (department_id) REFERENCES department (id);
ALTER TABLE employee ADD FOREIGN KEY (employee_position_id) REFERENCES employee_position (id);

ALTER TABLE employee_position ADD FOREIGN KEY (position_category_id) REFERENCES position_category (id);

ALTER TABLE course ADD FOREIGN KEY (department_id) REFERENCES department (id);

ALTER TABLE course_teacher ADD FOREIGN KEY (teacher_id) REFERENCES teacher (id);
ALTER TABLE course_teacher ADD FOREIGN KEY (course_id) REFERENCES course (id);

ALTER TABLE teacher ADD FOREIGN KEY (employee_id) REFERENCES employee (id);


ALTER TABLE schedule ADD FOREIGN KEY (semester_id) REFERENCES semester (id);
ALTER TABLE schedule ADD FOREIGN KEY (day_of_week_id) REFERENCES day_of_week (id);
ALTER TABLE schedule ADD FOREIGN KEY (control_point_id) REFERENCES control_point (id);
ALTER TABLE schedule ADD FOREIGN KEY (course_time_id) REFERENCES course_time (id);
ALTER TABLE schedule ADD FOREIGN KEY (course_teacher_id) REFERENCES course_teacher (id);
ALTER TABLE schedule ADD FOREIGN KEY (college_group_id) REFERENCES college_group (id);
ALTER TABLE schedule ADD FOREIGN KEY (lesson_type_id) REFERENCES lesson_type (id);

ALTER TABLE student_mark ADD FOREIGN KEY (schedule_id) REFERENCES schedule (id);
ALTER TABLE student_mark ADD FOREIGN KEY (student_id) REFERENCES student (id);
ALTER TABLE student_mark ADD FOREIGN KEY (control_type_id) REFERENCES control_type (id);
