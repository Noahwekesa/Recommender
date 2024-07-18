from django.urls import path
from . import views


urlpatterns = [
    path("", views.movie_list_view),
    path("<int:id>/", views.movie_detail_view),
]
