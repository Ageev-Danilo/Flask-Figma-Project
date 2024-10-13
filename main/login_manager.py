from flask_login import LoginManager
from .settings import project
from user.models import User


project.secret_key = "777"


login_manager = LoginManager(app = project)


@login_manager.user_loader
def load_user(id):
    return User.query.get(id)