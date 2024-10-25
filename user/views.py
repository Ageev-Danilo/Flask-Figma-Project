import flask, flask_login

from .models import User

from main.settings import data_base



def show_user_app():
    return flask.render_template(template_name_or_list = "user.html")

def show_login_page():

    if flask.request.method == "POST":
        username = flask.request.form["username"]
        password = flask.request.form["password"]
        users = User.query.all()


        for user in users:
            if user.username == username and user.password == password:
                flask_login.login_user(user = user)
                return flask.redirect("/")
        return flask.render_template(template_name_or_list = "login.html", incorrect = True)
    return flask.render_template(template_name_or_list = "login.html")

def show_reg_page():

    if flask.request.method == "POST":
        username = flask.request.form["username"]
        password = flask.request.form["password"]
        user = User(username = username, password = password)
        data_base.session.add(user)
        data_base.session.commit()
        return flask.render_template(template_name_or_list = "registration.html", send = True)
    


    return flask.render_template(template_name_or_list = "registration.html")