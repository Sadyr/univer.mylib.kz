from main_app.extension import db



class Person(db.Model):
    id = db.Column(db.Integer, primary_key = True,autoincrement=True)
    firstname = db.Column(db.String(80), nullable=False)
    lastname = db.Column(db.String(80), nullable=False)
    midlename = db.Column(db.String(80))
    birthday = db.Column(db.String(80), nullable=False)
    bio = db.Column(db.Text, nullable=False)
    picture = db.Column(db.String(250))
    gender_id = db.Column(db.Integer,db.ForeignKey('gender.id'),nullable=False)
    email = db.Column(db.String(80),unique=True, nullable=False)
    password = db.Column(db.String(80), nullable=False)
    phone_number = db.Column(db.String(80), nullable=False)
    person_group_id = db.Column(db.Integer, db.ForeignKey('person_group.id'), nullable=False)

    student = db.relationship('Student', backref='person', lazy=True)


    def __repr__(self):
        return f"<Person id: {self.id} and person firstname: {self.firstname}>"


class Gender(db.Model):
    id = db.Column(db.Integer, primary_key = True, autoincrement=True)
    name = db.Column(db.String(80),unique=True, nullable=False)

    person = db.relationship('Person', backref='gender',  lazy=True)

    def __repr__(self):
        return f"Gender id: {self.id}, and  gender name:{self.name}"
    
class Person_group(db.Model):
    id = db.Column(db.Integer, primary_key = True, autoincrement=True)
    name = db.Column(db.String(80),unique=True, nullable=False)

    person = db.relationship('Person', backref='person_group', lazy=True)

    def __repr__(self):
        return f"Person_group id: {self.id}, and  person_group name:{self.name}"
    
class Student(db.Model):
    id = db.Column(db.Integer, primary_key = True, autoincrement=True)
    person_id = db.Column(db.Integer, db.ForeignKey('person.id'),nullable=False)
    college_group_id = db.Column(db.Integer,db.ForeignKey('college_group.id'), nullable=False)

    def __repr__(self):
        return f"Student id: {self.id}, and  student person id:{self.person_id}"

class Curriculum(db.Model):
    id = db.Column(db.Integer, primary_key = True, autoincrement=True)
    name = db.Column(db.String(80),unique=True, nullable=False)
    description = db.Column(db.Text, nullable=False)

    speciality = db.relationship('Speciality', backref='curriculum', lazy=True)


    def __repr__(self):
        return f"Curriculum id: {self.id}, and  Curriculum  id:{self.name}"
    
class College_group(db.Model):
    id = db.Column(db.Integer, primary_key = True, autoincrement=True)
    name = db.Column(db.String(80),unique=True, nullable=False)
    grade_id = db.Column(db.Integer, db.ForeignKey('grade.id'),nullable=False)
    speciality_id = db.Column(db.Integer, db.ForeignKey('speciality.id'),nullable=False)

    student = db.relationship('Student', backref='college_group', lazy=True)


    def __repr__(self):
        return f"College_group id: {self.id}, and  College_group {self.name}"

class Grade(db.Model):
    id = db.Column(db.Integer, primary_key = True, autoincrement=True)
    name = db.Column(db.Integer,unique=True, nullable=False)
    college_group = db.relationship('College_group', backref='grade', lazy=True)

    def __repr__(self):
        return f"Grade id: {self.id}, and  Grade {self.name}"
    
class Speciality(db.Model):
    id = db.Column(db.Integer, primary_key = True, autoincrement=True)
    name = db.Column(db.String(200), nullable=False)
    code = db.Column(db.String(200),unique=True, nullable=False)
    curriculum_id = db.Column(db.Integer, db.ForeignKey('curriculum.id'),nullable=False)
    description = db.Column(db.Text, nullable=False)
    faculty_id = db.Column(db.Integer, db.ForeignKey('faculty.id'),nullable=False)

    speciality = db.relationship('College_group', backref='speciality', lazy=True)

    def __repr__(self):
        return f"Speciality id: {self.id}, and  Speciality {self.name}"



class Faculty(db.Model):
    id = db.Column(db.Integer, primary_key = True, autoincrement=True)
    name = db.Column(db.String(200),unique=True, nullable=False)
    description = db.Column(db.Text, nullable=False)

    speciality = db.relationship('Speciality', backref='faculty', lazy=True)
    department = db.relationship('Department', backref='faculty', lazy=True)

    def __repr__(self):
        return f"Faculty id: {self.id}, and  Faculty {self.name}"


class Department(db.Model):
    id = db.Column(db.Integer, primary_key = True, autoincrement=True)
    name = db.Column(db.String(200),unique=True, nullable=False)
    description = db.Column(db.Text, nullable=False)
    faculty_id = db.Column(db.Integer, db.ForeignKey('faculty.id'),nullable=False)
    employee = db.relationship('Employee', backref='department', lazy=True)


    def __repr__(self):
        return f"Department id: {self.id}, and  Department {self.name}"
    
class Employee(db.Model):
    id = db.Column(db.Integer, primary_key = True, autoincrement=True)
    person_id = db.Column(db.Integer, db.ForeignKey('person.id'),nullable=False)
    department_id = db.Column(db.Integer, db.ForeignKey('department.id'),nullable=False)
    employee_position_id = db.Column(db.Integer, db.ForeignKey('employee_position.id'),nullable=False)
    
    teacher = db.relationship('Teacher', backref='employee', lazy=True)

    def __repr__(self):
        return f"Employee id: {self.id}, and  Employee person {self.person_id}"
    
class Employee_position(db.Model):
    id = db.Column(db.Integer, primary_key = True, autoincrement=True)
    name = db.Column(db.String(200),unique=True, nullable=False)
    position_category_id = db.Column(db.Integer, db.ForeignKey('position_category.id'),nullable=False)

    employee = db.relationship('Employee', backref='employee_position', lazy=True)

    def __repr__(self):
        return  f"Employee_position id: {self.id}, and  Employee position {self.name}"

class Position_category(db.Model):
    id = db.Column(db.Integer, primary_key = True, autoincrement=True)
    name = db.Column(db.String(200),unique=True, nullable=False)

    employee_position = db.relationship('Employee_position', backref='position_category', lazy=True)

    def __repr__(self):
        return  f"Position_category id: {self.id}, and   position_category {self.name}"
    
class Teacher(db.Model):
    id = db.Column(db.Integer, primary_key = True, autoincrement=True)
    employee_id =  db.Column(db.Integer, db.ForeignKey('employee.id'),nullable=False)






    


















    




























    



    


    