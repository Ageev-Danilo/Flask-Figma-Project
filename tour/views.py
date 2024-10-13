import flask

from flask_login import current_user, logout_user

def render_tour_page():
    try:
        username = current_user.username
        if flask.request.method == "POST":
            if "logout_user" in flask.request.form:
                logout_user()
        else:
            return flask.render_template(template_name_or_list = "tour.html", username = username)
    except:
        pass


    return flask.render_template(template_name_or_list = "tour.html")