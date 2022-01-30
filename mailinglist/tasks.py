from art_work.celery import app
from .service import send

@app.task
def send_mess_email(user_email):
    send(user_email)
