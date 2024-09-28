import flask

def show_user_app():
    return flask.render_template(template_name_or_list = "user.html")