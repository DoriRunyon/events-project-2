from django.conf.urls import url
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    url(r'^$',  views.index, name='index'),
    url(r'^search/$', views.search_no_login, name='search_no_login'),
    url(r'^dashboard/$', views.logged_in_dashboard, name='logged_in_dashboard'),
]
