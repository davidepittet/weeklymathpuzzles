from django.urls import path, include
from . import views
from django.conf import settings
from django.contrib.staticfiles.urls import staticfiles_urlpatterns


urlpatterns = [
    path("", views.index),
    path("archive", views.archive, name="archive"), 
    path("leaderboard", views.leaderboard, name="leaderboard"), 
]

if settings.DEBUG:
    urlpatterns += staticfiles_urlpatterns()