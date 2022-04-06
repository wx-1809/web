


from post import views
from django.urls import path, re_path

urlpatterns = [
    path('', views.queryAll), #^$
    re_path(r'^page/(\d+)$', views.queryAll)
    # url(r'^page/(\d+)$', views.queryAll),
]