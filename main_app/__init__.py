import os
import psycopg2
import psycopg2.extras
from flask import Flask, render_template, request, url_for, redirect, session
from  config import Config
from main_app.models import *
def get_db_connections():
    conn = psycopg2.connect(host=os.environ['DATABASE_HOST'],
        database=os.environ['DATABASE_NAME'],
        user=os.environ['DB_USERNAME'],
        password=os.environ['DB_PASSWORD'])
    return conn


def create_app(config_class=Config):
#def create_app():

    # create and configure the app
    app = Flask(__name__)
    app.config.from_object(config_class)

    # Initialize Flask extension here

    # Register blueprints here
    from main_app.admin import bp as admin_bp
    app.register_blueprint(admin_bp)

    from main_app.teacher import bp as teacher_bp
    app.register_blueprint(teacher_bp)

    from main_app.student import bp as student_bp
    app.register_blueprint(student_bp)

    from main_app.auth import bp as auth_bp
    app.register_blueprint(auth_bp)
    
    # a simple page that says hello
    @app.route('/test')
    def hello():
        return render_template('test.html')
    return app



print(__name__)
if __name__ == '__main__':
    print('Hello world')
    print('Done')
    print(__name__)
    
"""     @app.route('/')
    def index():
        if session['person_group_id']:
            return user_group(int(session['person_group_id']))
        else:
            return redirect(url_for('auth.login'))
    


def user_group(person_group_id):
    if person_group_id == 1:
        return redirect(url_for('admin.index'))
    elif person_group_id == 2:
        return redirect(url_for('teacher.index'))
    else:
        return redirect(url_for('student.index'))
 """




""" @app.route('/')
def index():
    conn = get_db_connections()
    cur = conn.cursor(cursor_factory = psycopg2.extras.DictCursor)
    cur.execute('SELECT  firstname, lastname,midlename, birthday, gender.name as gender, email, password, phone_number, person_group.name, added'
' FROM person   INNER JOIN gender  ON person.gender_id=gender.id'
' INNER JOIN person_group ON person.person_group_id = person_group.id')
    persons = cur.fetchall()
    cur.close()
    conn.close()
    return render_template('index.html', persons=persons)


('SELECT  firstname, lastname,midlename, birthday, gender.name, email, password, phone_number, person_group_id'
'FROM person   JOIN gender  ON person.gender_id=gender.id;')

@app.route('/create/', methods=('GET', 'POST'))
def create():
    if request.method == 'POST':
        firstname = request.form['firstname']
        lastname = request.form['lastname']
        midlename = request.form['midlename']
        birthday = request.form['birthday']
        gender_id = request.form['gender_id']
        email = request.form['email']
        password = request.form['password']
        phone_number = request.form['phone_number']
        person_group_id = request.form['person_group_id']
        conn = get_db_connections()
        cur = conn.cursor()
        cur.execute('INSERT INTO person (firstname, lastname, midlename, birthday, gender_id, email, password, phone_number,person_group_id)'
                    'VALUES (%s, %s, %s, %s, %s, %s,%s, %s, %s)',
                    (firstname,lastname,midlename,birthday,gender_id,email,password,phone_number,person_group_id))
        conn.commit()
        cur.close()
        conn.close()
        return redirect(url_for('index'))
    return render_template('create.html')
 """



