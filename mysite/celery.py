import os
from celery import Celery
from mysite.core import tasks
DJANGO_SETTINGS_MODULE = 'mysite.settings'
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'mysite.settings')

app = Celery('mysite')
app.config_from_object('django.conf:settings', namespace='CELERY')
app.autodiscover_tasks(tasks.create_random_user_accounts)
