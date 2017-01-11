"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin

from bookmark.views import BookmarkLV, BookmarkDV
#from bookmark.views import *   # * 사용 가능

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    # url(r'^admin/', include(admin.site.urls)),
    # admin.site.urls 는 예외적으로 include() 함수를 사용하지 않아도 됨.

    # Class-based views for Bookmark app
    url(r'^bookmark/$', BookmarkLV.as_view(), name='index'),
    url(r'^bookmark/(?P<pk>\d+)$', BookmarkDV.as_view(), name='detail'),

    # url(regex, view, kwargs=None, name=None, prefix='')
    # 앞의 2개는 필수 인자, 뒤의 3개는 선택 인자.
    # patterns() 함수는 1.8 이후로 사용되지 않음.
]

# 간단한 로직은 아래와 같이 views.py 에서 처리하지 않고 바로 urls.py에서 처리 할 수도 있다.
# from django.views.generic import ListView, DetailView
# from bookmark.models import Bookmark

    # url(r'^bookmark/$', ListView.as_view(model=Bookmark), name='index'),
    # url(r'^bookmark/(?P<pk>\d+)$', DetailView.as_view(model=Bookmark), name='detail'),
