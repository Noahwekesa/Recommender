from django.urls import path
from . import views

app_name = "movies"

urlpatterns = [
    path("", views.movie_list_view, name="list"),
    path("infinite/", views.movie_infinite_rating_view, name="infinite"),
    path("<int:pk>/", views.movie_detail_view, name="detail"),
]
