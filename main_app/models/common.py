from sqlalchemy import Column, Integer, String, ForeignKey, Text
from sqlalchemy.orm import relationship

from main_app.models.database import Base


class College_group(Base):
    __tablename__ = 'college_group'
    id = Column(Integer, primary_key=True, unique=True, autoincrement=True)
    name = Column(String, nullable=False)
    grade_id =  Column(Integer, ForeignKey('grade.id'),nullable=False)
    speciality_id = Column(Integer, ForeignKey('speciality.id'),nullable=False)


    student = relationship('Student',back_populates="college_group", lazy='subquery')
    grade = relationship('Grade', back_populates="college_group", lazy='subquery')
    speciality = relationship('Speciality', back_populates="college_group", lazy='subquery')
    schedule = relationship('Schedule', back_populates="college_group")
    mark = relationship('Mark', back_populates="college_group")
    group_teacher_course =relationship ('Group_teacher_course', back_populates="college_group")
    rate = relationship('Rate',back_populates="college_group")


    


    def __repr__(self):
        return f'Студенческая группа  [ID: {self.id}, Название:{self.name}]'

class Gender(Base):
    __tablename__ = 'gender'
    id = Column(Integer, primary_key=True, unique=True, autoincrement=True)
    name = Column(String, nullable=False,unique=True)

    student = relationship('Student', back_populates="gender")
    teacher = relationship('Teacher', back_populates="gender")



class User_group(Base):
    __tablename__ = 'user_group'
    id = Column(Integer, primary_key=True, unique=True, autoincrement=True)
    name = Column(String, nullable=False)
    student = relationship('Student')


    
class Grade(Base):
    __tablename__ = 'grade'
    id = Column(Integer, primary_key=True, unique=True, autoincrement=True)
    name = Column(String, nullable=False, unique=True)

    college_group = relationship('College_group', back_populates="grade")


    
class Speciality(Base):
    __tablename__ = 'speciality'
    id = Column(Integer, primary_key=True, unique=True, autoincrement=True)
    name = Column(String, nullable=False)
    code = Column(String, nullable=False, unique=True)
    description = Column(Text, nullable=False)
    curriculum_id = Column(Integer, ForeignKey('curriculum.id'),nullable=False)
    faculty_id = Column(Integer, ForeignKey('faculty.id'),nullable=False)

    college_group = relationship('College_group', back_populates="speciality")
    curriculum = relationship('Curriculum', back_populates="speciality", lazy='subquery')
    faculty = relationship('Faculty', back_populates="speciality", lazy='subquery')




class Curriculum(Base):
    __tablename__ = 'curriculum'
    id = Column(Integer, primary_key=True, unique=True, autoincrement=True)
    name = Column(String,unique=True, nullable=False)
    description = Column(Text, nullable=False)


    speciality = relationship('Speciality', back_populates="curriculum", lazy='subquery')

class Faculty(Base):
    __tablename__ = 'faculty'
    id = Column(Integer, primary_key=True, unique=True, autoincrement=True)
    name = Column(String,unique=True, nullable=False)
    description = Column(Text, nullable=False)

    speciality = relationship('Speciality', back_populates="faculty")
    department = relationship('Department', back_populates="faculty")



class Department(Base):
    __tablename__ = 'department'
    id = Column(Integer, primary_key=True, unique=True, autoincrement=True)
    name = Column(String,unique=True, nullable=False)
    description = Column(Text, nullable=False)
    faculty_id = Column(Integer, ForeignKey('faculty.id'),nullable=False)

    faculty = relationship('Faculty', back_populates="department",lazy='subquery')
    teacher = relationship('Teacher', back_populates="department")
    course = relationship('Course', back_populates="department")


class Position(Base):
    __tablename__ = 'position'
    id = Column(Integer, primary_key=True, unique=True, autoincrement=True)
    name = Column(String,unique=True, nullable=False)

    teacher = relationship('Teacher', back_populates="position")