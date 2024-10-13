import flask
from .models import Tour

def render_tour_page():
    tours = Tour.query.all()
    return flask.render_template(template_name_or_list = "tour.html", tours = tours)

    
def render_view_tour_page(tour_id):
    tour_id = int(tour_id.split("=")[1])
    tour = Tour.query.get(tour_id)
    return flask.render_template(template_name_or_list = "view_tour.html", tour = tour)
    