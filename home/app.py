import flask

home = flask.Blueprint(
    import_name = "app",
    name =  "home_page",
    template_folder = "home/templates",
    static_folder = "static/home",
    static_url_path = "/"
)