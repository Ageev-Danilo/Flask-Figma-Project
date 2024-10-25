import flask

user_app = flask.Blueprint(
    name = "user",
    import_name = "app",
    template_folder = "user/templates",
    static_folder = "static",
    static_url_path = "/user/"
)