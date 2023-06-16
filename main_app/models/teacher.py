from sqlalchemy import Column, Integer, String, ForeignKey, Text
from main_app.models.database import Base
from sqlalchemy.orm import relationship

class Teacher(Base):
    __tablename__ = 'teacher'
    id = Column(Integer, primary_key=True, unique=True, autoincrement=True)
    firstname = Column(String, nullable=False)
    lastname = Column(String, nullable=False)
    middlename = Column(String, nullable=True)
    birthday = Column(String, nullable=False)
    bio =  Column(Text, nullable=False)
    picture = Column(Text, nullable=False)
    gender_id = Column(Integer, ForeignKey('gender.id'))
    email = Column(String, nullable=False)
    phone = Column(String, nullable=False)
    password = Column(String, nullable=False)
    user_group_id = Column(Integer, ForeignKey('user_group.id'))
    department_id = Column(Integer, ForeignKey('department.id'))
    position_id = Column(Integer, ForeignKey('position.id'),nullable=False)
    
    department = relationship('Department', back_populates="teacher", lazy='subquery')
    gender = relationship('Gender', back_populates="teacher", lazy='subquery')
    position = relationship('Position', back_populates="teacher", lazy='subquery')
    teacher_course = relationship('Teacher_course',back_populates="teacher")
    mark = relationship('Mark',back_populates="teacher")
    rate = relationship('Rate',back_populates="teacher")



    def __init__(self, firstname,
                  lastname,middlename,birthday,bio,picture,
                  gender_id, email,  phone, password,
                 user_group_id, department_id, position_id ):
        self.firstname = firstname
        self.lastname = lastname
        self.middlename = middlename
        self.birthday = birthday
        self.bio = bio
        self.picture = picture
        self.gender_id = gender_id
        self.email = email
        self.phone = phone
        self.password = password
        self.user_group_id = user_group_id
        self.department_id = department_id
        self.position_id = position_id

    def __repr__(self):
        info = f"Преподователь [ФИО: {self.firstname} {self.lastname} {self.middlename}]"
        return info








