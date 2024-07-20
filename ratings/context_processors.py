from .models import RatingChoice


def rating_choices(request):
    context = {"rating_choices": RatingChoice.values}
    return context
