#coding=utf-8

from post import views
from django.urls import path, re_path
# from django.conf.urls import url

urlpatterns = [
    path('', views.queryAll), #^$
    re_path(r'^page/(\d+)$', views.queryAll),
    # url(r'^page/(\d+)$', views.queryAll), post
    re_path(r'^post/(\d+)$', views.detail),
    re_path(r'^category/(\d+)$',views.queryPostByCid),
    re_path(r'^archive/(\d+)/(\d+)$',views.queryPostByCreated),

    # url(r'^$',views.queryAll),
    # url(r'^page/(\d+)$',views.queryAll),
    # url(r'^post/(\d+)$',views.detail),
    # url(r'^category/(\d+)$',views.queryPostByCid),
    # url(r'^archive/(\d+)/(\d+)$',views.queryPostByCreated),
]