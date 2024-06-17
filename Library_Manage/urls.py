from django.contrib import admin
from django.urls import include, path
from django.urls import path

urlpatterns = [
    path("", include("libraryapp.urls")),
    path("admin/", admin.site.urls),
]