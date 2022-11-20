from celery import Celery

app = Celery("shop_content")
app.config_from_object("django.conf.settings", namespace="CELERY")
app.autodiscover_tasks()
