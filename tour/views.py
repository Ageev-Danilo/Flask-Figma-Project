import flask
from .models import Tour
from flask_login import current_user, logout_user

def render_tour_page():
    tours = Tour.query.all()
    try:
        username = current_user.username
        if flask.request.method == "POST":
            if "logout_user" in flask.request.form:
                logout_user()
        else:
            return flask.render_template(template_name_or_list = "tour.html", username = username, tours = tours)
    except:
        pass


    return flask.render_template(template_name_or_list = "tour.html", tours = tours)
    
def render_view_tour_page(tour_id):
    tour_id = int(tour_id.split("=")[1])
    tour = Tour.query.get(tour_id)
    try:
        username = current_user.username
        if flask.request.method == "POST":
            if "logout_user" in flask.request.form:
                logout_user()
        else:
            return flask.render_template(template_name_or_list = "tour.html", username = username, tour = tour)
    except:
        pass
    return flask.render_template(template_name_or_list = "view_tour.html", tour = tour)
    