from sqlalchemy import Column, Integer, String, ForeignKey, Text

from database import Base
from sqlalchemy.orm import relationship

class Student(Base):
    __tablename__ = 'student'
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
    college_group_id = Column(Integer, ForeignKey('college_group.id'))

    college_group = relationship('College_group',back_populates="student", lazy='subquery')
    gender = relationship('Gender', back_populates="student", lazy='subquery')
    portfolio = relationship('Portfolio', back_populates="student")

    mark = relationship('Mark',back_populates="student")
    rate = relationship('Rate',back_populates="student")




    def __init__(self, firstname,
                  lastname,middlename,birthday,bio,picture,
                  gender_id, email,  phone, password,
                 user_group_id, college_group_id ):
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
        self.college_group_id = college_group_id

    def __repr__(self):
        info = f"Студент [ФИО: {self.firstname} {self.lastname} {self.middlename}]"
        return info









