import csv

from django.conf import settings
from django.core.mail import EmailMessage

from main_app.celery import app

FROM_EMAIL = settings.DEFAULT_FROM_EMAIL


@app.task
def generate_csv_file(filename, data):
    try:
        with open(filename, "w", newline="\n") as file:
            csv_writer = csv.DictWriter(file, fieldnames=data[0].keys())
            csv_writer.writeheader()
            csv_writer.writerows(data)

        return filename
    except Exception as e:
        return str(e)


@app.task
def send_email(subject, message, receivers, file_path=None):
    email = EmailMessage(
        subject,
        message,
        FROM_EMAIL,
        receivers,
    )

    if file_path:
        email.attach_file(file_path)

    email.send()
