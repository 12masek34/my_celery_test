import os
from celery import Celery
from celery.schedules import crontab

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'app_project.settings')

app = Celery('app_project')
app.config_from_object('django.conf:settings', namespace='CELERY')
app.autodiscover_tasks()

# celery beat task

app.conf.beat_schedule = {
    'send-spam-every-3-minute': {
        'task': 'my_celery_app.tasks.send_beat_email',
        'schedule': crontab(minute='*/3')
    },
}
