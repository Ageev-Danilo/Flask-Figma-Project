import flask

user_app = flask.Blueprint(
    name = "user_app",
    import_name = "user",
    template_folder = "templates"
)