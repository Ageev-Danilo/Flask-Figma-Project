from main.settings import data_base
from flask_login import UserMixin


class User(data_base.Model, UserMixin):
    id = data_base.Column(data_base.Integer, primary_key = True)
    username = data_base.Column(data_base.String(100), nullable = False)
    password = data_base.Column(data_base.String(50), nullable = False)
    