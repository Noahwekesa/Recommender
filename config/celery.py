import os


from celery import Celery

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "config.settings")

app = Celery("config")

app.config_from_object("django.conf:settings", namespace="CELERY")


app.autodiscover_tasks()


app.conf.beat_schedule = {
    "run_movie_rating_avg_every_30": {
        "task": "task_calculate_movie_ratings",
        "schedule": 60 * 30,  # 30 mins
        "kwargs": {"all": 20_000},
    }
}
