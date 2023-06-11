from flask import render_template
from main_app.student import bp
from main_app.auth import routes


@bp.route('/')
@routes.login_required
def index():
    return render_template('student/index.html')

