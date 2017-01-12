from django.contrib import admin
from blog.models import Post

# Register your models here.

# 관리자 화면에서 보여질 모습 정의
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'modify_date')  # 리스트화면에서 보여줄 컬럼 정의
    list_filter = ('modify_date',) # 필터사이드바 사용할 컬럼 정의
    search_fields = ('title', 'content') # 검색박스 사용 및 검색 시 적용할 컬럼 정의
    prepopulated_fields = {'slug': ('title',)} # slug필드는 title을 이용해 미리 채워지도록 설정

admin.site.register(Post, PostAdmin)
