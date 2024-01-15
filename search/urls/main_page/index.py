from django.urls import path
from search.views.main_page.get_info import get_info
from search.views.main_page.login import signin
from search.views.main_page.logout import signout
from search.views.main_page.register import register
from search.views.main_page.get_status import get_status
from search.views.main_page.get_suggestions import get_suggestions


urlpatterns = [
    path("get_info/", get_info, name="main_page_get_info"),
    path("login/", signin, name="main_page_login"),
    path("logout/", signout, name="main_page_logout"),
    path("register/", register, name="main_page_register"),
    path("get_status/", get_status, name="main_page_get_status"),
    path("get_suggestions/", get_suggestions, name="main_page_get_suggestions"),
]
