from django.apps import AppConfig


class first_appConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'first_app'

    def ready(self):
       import first_app.signals  # Signalları aktiv edin
       return super().ready()



