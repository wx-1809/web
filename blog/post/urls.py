

from django.conf.urls import url
from post import views
from django.urls import path

urlpatterns = [
    path(r'^$', views.queryAll) #^$
]