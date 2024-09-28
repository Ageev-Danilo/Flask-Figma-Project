import flask

home = flask.Blueprint(
    import_name = "home",
    name =  "home_page",
    template_folder = "home/templates"
)