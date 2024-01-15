from django.urls import path, include, re_path
from search.views.index import index
from django.contrib import admin


urlpatterns = [
    path("", index, name="index"),
    path("main_page/", include("search.urls.main_page.index")),
    path("admin/", admin.site.urls, name="admin"),


    re_path(r".*", index, name="index"),
]

