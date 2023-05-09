import os
import requests
from dotenv import load_dotenv
import jinja2

load_dotenv()

DOMAIN = os.getenv("MAILGUN_DOMAIN")
template_loader = jinja2.FileSystemLoader("templates")
template_env = jinja2.Environment(loader=template_loader)


# How to send HTML emails using Mailgun and Python
def render_template(template_filename, **context):
    return template_env.get_template(template_filename).render(**context)


# How to send emails with Python and Mailgun
# How to populate and consume the task queues with rq
def send_simple_message(to, subject, body, html):
    return requests.post(
        f"https://api.mailgun.net/v3/{DOMAIN}/messages",
        auth=("api", os.getenv("MAILGUN_API_KEY")),
        data={
            "from": f"Lewis Chen <mailgun@{DOMAIN}>",
            "to": [to],
            "subject": subject,
            "text": body,
            "html": html,
        },
    )


# How to send emails when users register
# How to populate and consume the task queues with rq
def send_user_registration_email(email, username):
    return send_simple_message(
        email,
        "Successfully signed up",
        f"Hi {username}! You have successfully signed up to the Stores REST API.",
        render_template("email/registration.html", username=username),
    )
