from django.views.generic import ListView, DetailView, TemplateView
from django.views.generic.dates import ArchiveIndexView, YearArchiveView, MonthArchiveView, DayArchiveView, TodayArchiveView

from tagging.models import Tag, TaggedItem
from tagging.views import TaggedObjectList

from blog.models import Post

# Create your views here.

#--- TemplateView
class TagTV(TemplateView):
    template_name = 'tagging/tagging_cloud.html'

#--- ListView
class PostLV(ListView):
    model = Post
    template_name = 'blog/post_all.html' # 사용할 템플릿 정의, default blog/post_list.html _list 붙여주게됨.
    context_object_name = 'posts' # 템플릿으로 넘겨줄 컨텍스트 변수명을 정의, default명은 object_list
    paginate_by = 2 # 한페이지에 보여주게 되는 갯수 정의

class PostTOL(TaggedObjectList):
    model = Post
    template_name = 'tagging/tagging_post_list.html'

#--- DetailView
class PostDV(DetailView): # 기본키 대신 slug로 상세 정보를 추출.
    model = Post

#--- ArchiveView
class PostAV(ArchiveIndexView): # 날짜 필드를 기준으로 정렬, 내림차순
    model = Post
    date_field = 'modify_date' # dateqeurySet에 사용할 컬럼 정의
    # Entry.objects.dates('modify_date') 이런 쿼리셋이 사용되는걸까?
    # 모델명_archive.html default 템플릿으로 사용
    # context 접근 변수로 date_list 사용

class PostYAV(YearArchiveView): # 날짜중 연도를 기준으로 정렬
    # Entry.objects.dates('modify_date', 'year') ?
    model = Post
    date_field = 'modify_date'
    make_object_list = True # 해당년도와 일치하는 객체 리스트를 넘겨줌, object_list로 사용, default=False
    # 모델명_archive_year.html default 템플릿으로 사용

class PostMAV(MonthArchiveView):
    model = Post
    date_field = 'modify_date'
    # 모델명_archive_month.html default 템플릿으로 사용

class PostDAV(DayArchiveView):
    model = Post
    date_field = 'modify_date'
    # 모델명_archive_day.html default 템플릿으로 사용

class PostTAV(TodayArchiveView):
    model = Post
    date_field = 'modify_date'
    # 모델명_archive_day.html default 템플릿으로 사용, DayArchiveView 제네릭과 동일한 뷰 사용하는 것에 주의.
    # url에 /blog/today 라고 하면 이리 실행
