from django.apps import apps
from django.contrib.contenttypes.models import ContentType
from celery import shared_task
from movies.models import Movie
from accounts import utils as profile_utils
from . import utils as ml_utils


@shared_task
def train_surprise_model_task():
    ml_utils.train_surprise_model()


@shared_task
def batch_users_prediction_task(
    users_ids=None,
    start_page=0,
    offset=50,
    max_pages=1000,
):
    model = ml_utils.load_model()
    Suggestion = apps.get_model("suggestions", "Suggestion")
    ctype = ContentType.objects.get(app_label="movies", model="movie")
    end_page = start_page + offset
    if users_ids is None:
        users_ids = profile_utils.get_recent_users()
    movie_ids = (
        Movie.objects.all().popular().values_list(
            "id", flat=True)[start_page:end_page]
    )
    recently_suggested = Suggestion.objects.get_recently_suggested(
        movie_ids, users_ids)
    new_suggestion = []
    for movie_id in movie_ids:
        users_done = recently_suggested.get(f"{movie_id}") or []
        for u in users_ids:
            if u in users_done:
                continue
            pred = model.predict(uid=u, iid=movie_id).est
            data = {
                "user_id": u,
                "object_id": movie_id,
                "value": pred,
                "content_type": ctype,
            }
            new_suggestion.append(Suggestion(**data))
    Suggestion.objects.bulk_create(new_suggestion, ignore_conflicts=True)
    if end_page < max_pages:
        return batch_users_prediction_task(start_page=end_page - 1)


@shared_task
def batch_single_user_predictions_task(
    user_id=1, start_page=0, offset=250, max_pages=100_000
):
    return batch_users_prediction_task(
        users_ids=[
            user_id], start_page=start_page, offset=offset, max_pages=max_pages
    )
