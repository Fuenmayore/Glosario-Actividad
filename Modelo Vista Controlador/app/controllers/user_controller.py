from flask import Blueprint, render_template
from app.models.user_model import get_users

user_blueprint = Blueprint('user', __name__)

@user_blueprint.route('/users')
def list_users():
    users = get_users()
    return render_template('user_view.html', users=users)
