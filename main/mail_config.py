from .settings import project
import flask, flask_mail

ADMINISTRATION_ADRESS = "termaks2000@gmail.com"
ADMINISTRATION_PASSWORD = "gdpb jxyr xkjk plfd"
USER_ADRESS = "m.tereshonok2010@gmail.com"

project.config["MAIL_SERVER"] = "smtp.gmail.com"
project.config["MAIL_PORT"] = 587
project.config["MAIL_USE_TLS"] = True
project.config["MAIL_USERNAME"] = ADMINISTRATION_ADRESS
project.config["MAIL_PASSWORD"] = ADMINISTRATION_PASSWORD

mail = flask_mail.Mail(app = project)