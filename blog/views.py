from django.views.generic import ListView, DetailView, TemplateView
from django.views.generic.dates import ArchiveIndexView, YearArchiveView, MonthArchiveView, DayArchiveView, TodayArchiveView

from tagging.models import Tag, TaggedItem
from tagging.views import TaggedObjectList

from django.views.generic.edit import FormView
from blog.forms import PostSearchForm
from django.db.models import Q
from django.shortcuts import render

from blog.models import Post
from bookmark.models import Bookmark

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

class SearchFormView(FormView):
    # FormView 제네릭 뷰는 요청 받으면
    # GET 방식일 경우 걍 클래스 로직을 타고 흘러감
    # POST 방식일 경우 데이터가 적절한지 확인하고 form_valid() 함수를 실행시킴
    form_class = PostSearchForm
    template_name = 'blog/post_search.html'

    def form_valid(self, form):
        schWord = '%s' % self.request.POST['search_word']
        post_list = Post.objects.filter(Q(title__icontains=schWord)
            | Q(description__icontains=schWord)
            | Q(content__icontains=schWord)).distinct()

        bookmark_list = Bookmark.objects.filter(Q(title__icontains=schWord)).distinct()
        # Q객체는 매칭 조건을 다양하게 줄 수 있도록 한다.
        # icontains는 대소문자 구분없이 단어가 포함되어 있다면 추출 (LIKE 연산자같이?)
        # distinct() 함수는 중복 값은 제거 한다.

        context = {}
        context['form'] = form
        context['search_term'] = schWord
        context['object_list'] = post_list
        context['bookmark_list'] = bookmark_list
        return render(self.request, self.template_name, context)
