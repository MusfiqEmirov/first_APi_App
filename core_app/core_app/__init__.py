from __future__ import absolute_import, unicode_literals

# bu, Django'nun Celery tətbiqini avtomatik olaraq yükləməsi üçün vacibdir
from .celery import app as celery_app

__all__ = ('celery_app',)
