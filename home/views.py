import flask
from flask_mail import Message
from main.mail_config import mail, ADMINISTRATION_ADRESS, USER_ADRESS



from flask_login import current_user, logout_user

def render_home_page():
    try:
        username = current_user.username
        if flask.request.method == "POST":
            print(list(flask.request.form))
            if "logout_user" in flask.request.form:
                logout_user()
                return flask.render_template(template_name_or_list = "home.html")
        else:
            return flask.render_template(template_name_or_list = "home.html", username = username)
    except:
        pass
    if flask.request.method == "POST":
        if "logout_user" not in flask.request.form:
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
