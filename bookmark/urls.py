from django.conf.urls import url

from bookmark.views import BookmarkLV, BookmarkDV

urlpatterns = [
    url(r'^$', BookmarkLV.as_view(), name='index'),  # url 패턴 이름은 bookmark:index 가 된다.
    url(r'^(?P<pk>\d+)$', BookmarkDV.as_view(), name='detail'), # bookmark:detail
]
