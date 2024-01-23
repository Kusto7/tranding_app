import smtplib
from email.message import EmailMessage

from celery import Celery
from config import EMAIL_HOST_USER, EMAIL_HOST_PASSWORD, EMAIL_HOST, EMAIL_PORT

celery = Celery('tasks', broker='redis://localhost:6379')


def get_email_template_test(username: str):
    email = EmailMessage()
    email['Subject'] = 'Test Email'
    email['From'] = EMAIL_HOST_USER
    email['To'] = EMAIL_HOST_USER

    email.set_content(
        '<div>'
        f'<h1 style="color: red;">Здравствуйте, {username}! Тестовое письмо!</h1>'
        '</div>',
        subtype='html'
    )
    return email


# @celery.task()
def send_email_report_test(username: str):
    email = get_email_template_test(username)
    with smtplib.SMTP_SSL(EMAIL_HOST, EMAIL_PORT) as server:
        server.login(EMAIL_HOST_USER, EMAIL_HOST_PASSWORD)
        server.send_message(email)
