from flask import render_template
from main_app.teacher import bp
from main_app.auth import routes


@bp.route('/')
@routes.login_required

def index():
    return 'THis is teacher content'

