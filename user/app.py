import flask

user_qapp = flask.Blueprint(
    name = "user_app",
    import_name = "user_app",
    template_folder = "user_app/templates"
)