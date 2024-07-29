from django.contrib import admin
from django.urls import include, path

# from django.conf import settings
# from django.conf.urls.static import static
from ratings import views as ratings_views

urlpatterns = [
    path("", include("pages.urls")),
    path("accounts/", include("allauth.urls")),
    path("admin/", admin.site.urls),
    path("movies/", include("movies.urls")),
    path("rate/movie/", ratings_views.rate_movie_view),
]

# urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
