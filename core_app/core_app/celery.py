from __future__ import absolute_import, unicode_literals
import os
from celery import Celery

# Django settings modulunu göstəririk
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'core_app.settings')

app = Celery('core_app')

# Django'yu Celery ilə inteqrasiya edirik
app.config_from_object('django.conf:settings', namespace='CELERY')

# Celery'yi Django model və task-larını tapmaq üçün konfiqurasiya edirik
app.autodiscover_tasks()
