from flask import Blueprint

bp = Blueprint('teacher', __name__,
               url_prefix='/teacher',
               template_folder='templates',
               static_folder='static')

from main_app.teacher import routes