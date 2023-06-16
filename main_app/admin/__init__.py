from flask import Blueprint

bp = Blueprint('admin', __name__,
                url_prefix='/admin',
               template_folder='templates',
               static_folder='static')

from main_app.admin import routes
from main_app.admin.views import student, faculty, speciality, department, group, teacher, course, mark, report
