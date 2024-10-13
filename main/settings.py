import flask
import os
import flask_sqlalchemy, flask_migrate
project = flask.Flask(
    import_name = "main",
    template_folder = "templates",
    instance_path = os.path.abspath(__file__ + "/../../instance")
)

project.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///data.db"

data_base = flask_sqlalchemy.SQLAlchemy(app = project)
migrate = flask_migrate.Migrate(app = project, db = data_base)