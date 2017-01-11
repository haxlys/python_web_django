from django.views.generic import ListView, DetailView
from bookmark.models import Bookmark

# Create your views here.

#--- ListView
class BookmarkLV(ListView):
    model = Bookmark
# ListView 에서 자동으로 설정해주는 2가지
# 1. 컨텍스트 변수로 object_list 사용
# 2. 템플릿으로 모델명소문자_list.html 사용

#--- DetailView
class BookmarkDV(DetailView):
    model = Bookmark
# DetailView 에서 자동으로 설정해주는 2가지
# 1. 컨텍스트 변수로 object 사용
# 2. 템플릿으로 모델명소문자_detail.html 사용


# 리턴해주는 템플릿이과 컨텍스트 변수가 없지만 자동으로 설정해줌
# 디테일 같은 경우에는 url로 부터 넘어오는 매개변수를 통해서 가져온다고 함. urls.py에 정의한 매개변수명(pk)을 변경해도 인식할까?
# pk는 장고가 인식하는 고유의 변수명 같다. 다른 변수명을 명시할 경우 에러를 발생시킨다.
