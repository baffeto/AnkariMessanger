from celery import Celery
from django.conf import settings
import os
import datetime
import time


os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'ankari.settings')

app = Celery('ankari')
app.config_from_object('django.conf:settings')
app.conf.broker_url = settings.CELERY_BROCKER_URL
app.autodiscover_tasks()


@app.task()
def debug_task():
    time.sleep(20)
    now = datetime.datetime.now()
    print(f'Ankari: {now}')