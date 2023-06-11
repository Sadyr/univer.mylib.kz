from flask import Blueprint

bp = Blueprint('student', __name__,
               url_prefix='/student',
               template_folder='templates',
               static_folder='static')

from main_app.student import routes