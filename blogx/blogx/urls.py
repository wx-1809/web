"""blogx URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.urls import path, include, re_path
# from django.conf.urls import url, include

from blogx.settings import DEBUG,MEDIA_ROOT

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('post.urls')), #^
    path('ckeditor/',include('ckeditor_uploader.urls')),
    # path('search/',include('haystack.urls'))
    # url(r'^admin/', admin.site.urls),
    # url(r'^', include('post.urls')),
    # url(r'ckeditor/', include('ckeditor_uploader.urls')),
    # url(r'search/',include('haystack.urls'))
]

from django.views.static import serve
if DEBUG:
    urlpatterns+=re_path(r'^media/(?P<path>.*)/$', serve, {"document_root": MEDIA_ROOT}),

# from django.views.static import serve
# if DEBUG:
#     urlpatterns+=url(r'^media/(?P<path>.*)/$', serve, {"document_root": MEDIA_ROOT}),