import flask
from flask_mail import Message
from main.mail_config import mail, ADMINISTRATION_ADRESS, USER_ADRESS



def render_home_page():
    if flask.request.method == "POST":
        client_name = flask.request.form["client_name"]
        client_review = flask.request.form["client_review"]
        client_email = flask.request.form["client_email"]
        send_message = Message(
            subject = "Відгук", sender = ADMINISTRATION_ADRESS, recipients = [USER_ADRESS], body = f"""
                Клієнт {client_name} залишив/ла відгук:

                {client_review}.

                Пошта для зворотнього звʼязку з клієнтом {client_email}."""
            )
        mail.send(message = send_message)
    return flask.render_template(template_name_or_list = "home.html")