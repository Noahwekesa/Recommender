from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path("accounts/", include("allauth.urls")),
    path("", include("pages.urls")),
    path("admin/", admin.site.urls),
]
