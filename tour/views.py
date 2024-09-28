import flask

def render_tour_page():
    return flask.render_template(template_name_or_list = "tour.html")