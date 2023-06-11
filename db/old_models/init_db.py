from main_app.extension import db
from main_app.models.models import Person, Gender


gender1 = Gender(name='Male')
gender2 = Gender(name='Female')

person1  = Person(
    firstname = 'Sadyr',
    lastname = 'ABC',
    midlename = 'ABC',
    birthday = 'ABC',
    bio = 'ABC',
    picture = 'ABC',
    gender_id =  1,
    email = 'ABdC',
    password = 'ABC',
    phone_number = 'ABC',
    person_group_id = 1
    )

person2  = Person(
    firstname = 'Ivan',
    lastname = 'ABC',
    midlename = 'ABC',
    birthday = 'ABC',
    bio = 'ABC',
    picture = 'ABC',
    gender_id =  1,
    email = 'ABsC',
    password = 'ABC',
    phone_number = 'ABC',
    person_group_id = 1
    )
person3  = Person(
    firstname = 'Lena',
    lastname = 'ABC',
    midlename = 'ABC',
    birthday = 'ABC',
    bio = 'ABC',
    picture = 'ABC',
    gender_id =  2,
    email = 'ABedxC',
    password = 'ABC',
    phone_number = 'ABC',
    person_group_id = 1
    )


person4  = Person(
    firstname = 'John',
    lastname = 'ABC',
    midlename = 'ABC',
    birthday = 'ABC',
    bio = 'ABC',
    picture = 'ABC',
    gender_id =  1,
    email = 'ABerddsC',
    password = 'ABC',
    phone_number = 'ABC',
    person_group_id = 1
    )

person5  = Person(
    firstname = 'Syzi',
    lastname = 'ABC',
    midlename = 'ABC',
    birthday = 'ABC',
    bio = 'ABC',
    picture = 'ABC',
    gender_id =  2,
    email = 'ABdkksC',
    password = 'ABC',
    phone_number = 'ABC',
    person_group_id = 1
    )
person6 = Person(
    firstname = 'Milli',
    lastname = 'ABC',
    midlename = 'ABC',
    birthday = 'ABC',
    bio = 'ABC',
    picture = 'ABC',
    gender_id =  2,
    email = 'dlkede',
    password = 'ABC',
    phone_number = 'ABC',
    person_group_id = 1
    )

gender1 = Gender( name='Male')
gender2 = Gender( name='Female')

db.session.add_all([gender1, gender2])
db.session.add_all([person1, person2, person3, person4, person5])

db.session.commit()