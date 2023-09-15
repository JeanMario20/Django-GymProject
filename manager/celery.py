from __future__ import absolute_import, unicode_literals

import os 
from celery import Celery

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'manager.settings')
app = Celery('manager')
app.config_from_object('django.conf:settings', namespace='CELERY')
app.autodiscover_tasks()




@app.task(bind=True, ingore_result=True)
def debug_task(self):
    print(f'request:{self.request!r}')

app.conf.beat_schedule = {
    'update-every-ten-seconds': {
        'task': 'gymLogistic.task.actualizar_dato_periodicamente',
        'schedule': 10.0,
    },
}