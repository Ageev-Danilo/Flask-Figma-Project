import flask
import os
import flask_sqlalchemy, flask_migrate
project = flask.Flask(
    import_name = "settings",
    template_folder = "main/templates",
    instance_path = os.path.abspath(__file__ + "/../../instance"),
    static_folder = "static"
)

project.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///data.db"

data_base = flask_sqlalchemy.SQLAlchemy(app = project)
migrate = flask_migrate.Migrate(app = project, db = data_base)