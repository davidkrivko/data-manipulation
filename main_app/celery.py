import os
from celery import Celery


# Set the default Django settings module for the 'celery' program.
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "main_app.settings")

# Create a Celery instance.
app = Celery("app")
app.config_from_object("django.conf:settings", namespace="CELERY")

app.autodiscover_tasks()
