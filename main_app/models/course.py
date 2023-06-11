from sqlalchemy import Column, Integer, String, ForeignKey, Text

from main_app.models.database import Base
from sqlalchemy.orm import relationship
from sqlalchemy import UniqueConstraint



class Course(Base):
    __tablename__ = 'course'
    id = Column(Integer, primary_key=True, unique=True, autoincrement=True)
    name = Column(String, nullable=False, unique=True)
    shortname = Column(String, nullable=False, unique=True)
    credit_hours = Column(Integer, nullable=False)
    theoretical_hours = Column(Integer, nullable=False)
    experimental_hours = Column(Integer, nullable=False)
    description =  Column(Text, nullable=False)
    department_id = Column(Integer, ForeignKey('department.id'))

    department = relationship('Department',back_populates="course", lazy='subquery')
    teacher_course = relationship('Teacher_course',back_populates="course")
    mark = relationship('Mark',back_populates="course")



    def __init__(self, name,
                  shortname,credit_hours,theoretical_hours,experimental_hours,
                  description, department_id):
        self.name = name
        self.shortname = shortname
        self.credit_hours = credit_hours
        self.theoretical_hours = theoretical_hours
        self.experimental_hours = experimental_hours
        self.description = description
        self.department_id = department_id
      

    def __repr__(self):
        info = f"Курс [ {self.name} {self.shortname}]"
        return info

class Teacher_course(Base):
    __tablename__ = 'teacher_course'
    id = Column(Integer, primary_key=True, unique=True, autoincrement=True)
    teacher_id = Column(Integer, ForeignKey('teacher.id'))
    course_id = Column(Integer, ForeignKey('course.id'))


    teacher = relationship('Teacher',back_populates="teacher_course", lazy='subquery')
    course = relationship('Course',back_populates="teacher_course", lazy='subquery')
    schedule = relationship('Schedule',back_populates="teacher_course", lazy='subquery')
    mark = relationship('Mark',back_populates="teacher_course",lazy='subquery')
    group_teacher_course =relationship ('Group_teacher_course', back_populates="teacher_course", lazy='subquery')


class Group_teacher_course(Base):
    __tablename__ = 'group_teacher_course'
    id = Column(Integer, primary_key=True, unique=True, autoincrement=True)
    teacher_course_id = Column(Integer, ForeignKey('teacher_course.id'))
    college_group_id = Column(Integer, ForeignKey('college_group.id'))
    semester_id = Column(Integer, ForeignKey('semester.id'))

    teacher_course = relationship('Teacher_course',back_populates="group_teacher_course", lazy='subquery')
    semester = relationship('Semester',back_populates="group_teacher_course", lazy='subquery')
    college_group = relationship('College_group',back_populates="group_teacher_course", lazy='subquery')


#class Mark(Base):
 #   __tablename__ = 'mark'
 #   id = Column(Integer, primary_key=True, unique=True, autoincrement=True)
  #  teacher_course_id = Column(Integer, ForeignKey('teacher_course.id'))
  #  college_group_id = Column(Integer, ForeignKey('college_group.id'))


   # teacher_course = relationship('Teacher_course',back_populates="mark", lazy='subquery')
   # college_group = relationship('College_group',back_populates="mark", lazy='subquery')

class Mark(Base):
    __tablename__ = 'mark'
    id = Column(Integer, primary_key=True, unique=True, autoincrement=True)
    student_id = Column(Integer, ForeignKey('student.id'))
    college_group_id = Column(Integer, ForeignKey('college_group.id'))
    course_id = Column(Integer, ForeignKey('course.id'))
    teacher_id = Column(Integer, ForeignKey('teacher.id'))
    control_point_id=Column(Integer, ForeignKey('control_point.id'))
    semester_id = Column(Integer, ForeignKey('semester.id'))
    mark = Column(Integer, nullable=False)
    teacher_course_id = Column(Integer, ForeignKey('teacher_course.id'))

    student = relationship('Student',back_populates="mark", lazy='subquery')
    college_group = relationship('College_group',back_populates="mark", lazy='subquery')
    course = relationship('Course',back_populates="mark", lazy='subquery')
    teacher = relationship('Teacher',back_populates="mark", lazy='subquery')
    control_point = relationship('Control_point',back_populates="mark", lazy='subquery')
    semester = relationship('Semester',back_populates="mark", lazy='subquery')
    teacher_course = relationship('Teacher_course',back_populates="mark", lazy='subquery')




class Schedule(Base):
    __tablename__ = 'schedule'
    id = Column(Integer, primary_key=True, unique=True, autoincrement=True)
    teacher_course_id = Column(Integer, ForeignKey('teacher_course.id'))
    college_group_id = Column(Integer, ForeignKey('college_group.id'))
    semester_id = Column(Integer, ForeignKey('semester.id'))
    day_of_week_id = Column(Integer, ForeignKey('day_of_week.id'))
    lesson_time_id = Column(Integer, ForeignKey('lesson_time.id'))
    lesson_type_id = Column(Integer, ForeignKey('lesson_type.id'))
    room = Column(Integer, nullable=False)


    teacher_course = relationship('Teacher_course',back_populates="schedule", lazy='subquery')
    college_group = relationship('College_group',back_populates="schedule", lazy='subquery')
    semester = relationship('Semester',back_populates="schedule", lazy='subquery')
    day_of_week = relationship('Day_of_week',back_populates="schedule",lazy='subquery')
    lesson_time = relationship('Lesson_time',back_populates="schedule", lazy='subquery')
    lesson_type = relationship('Lesson_type',back_populates="schedule", lazy='subquery')
    
    UniqueConstraint('teacher_course_id', 'lesson_time_id', 'day_of_week_id', name='teacher_time_day')


class Semester(Base):
    __tablename__ = 'semester'
    id = Column(Integer, primary_key=True, unique=True, autoincrement=True)
    name = Column(String, nullable=False)
    start_date = Column(String, nullable=False)
    end_date =  Column(String, nullable=False)

    schedule = relationship('Schedule',back_populates="semester")
    group_teacher_course =relationship ('Group_teacher_course', back_populates="semester")
    mark = relationship('Mark',back_populates="semester")


class Control_point(Base):
    __tablename__ = 'control_point'
    id = Column(Integer, primary_key=True, unique=True, autoincrement=True)
    name = Column(String, nullable=False)
    start_date = Column(String, nullable=False)
    end_date =  Column(String, nullable=False)

    mark = relationship('Mark',back_populates="control_point")




class Day_of_week(Base):
    __tablename__ = 'day_of_week'
    id = Column(Integer, primary_key=True, unique=True, autoincrement=True)
    name = Column(String, nullable=False)


    schedule = relationship('Schedule',back_populates="day_of_week")  

class Lesson_time(Base):
    __tablename__ = 'lesson_time'
    id = Column(Integer, primary_key=True, unique=True, autoincrement=True)
    name = Column(String, nullable=False)


    schedule = relationship('Schedule',back_populates="lesson_time") 

class Lesson_type(Base):
    __tablename__ = 'lesson_type'
    id = Column(Integer, primary_key=True, unique=True, autoincrement=True)
    name = Column(String, nullable=False)


    schedule = relationship('Schedule',back_populates="lesson_type") 