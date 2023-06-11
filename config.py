import os
basedir = os.path.abspath(os.path.dirname(__file__))

class Config:
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URI')
    SECRET_KEY = os.environ['SECRET_KEY']
    HOST=os.environ['DATABASE_HOST'] 
    DATABASE= os.environ['DATABASE_NAME']    
    USER=os.environ['DB_USERNAME'],
    PASSWORD=os.environ['DB_PASSWORD']