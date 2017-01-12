from django.contrib import admin
from photo.models import Album, Photo

# Register your models here.
class PhotoInline(admin.StackedInline): # StackedInline(세로보기) 사진을 보여줄 형식 정의, Tabularinline 형식은 테이블 형식
    model = Photo
    extra = 2 # 추가 입력 객체수

class AlbumAdmin(admin.ModelAdmin):
    inlines = [PhotoInline] # PhotoInline 클래스에 정의된 내용을 보여준다.
    list_display = ('name', 'description')

class PhotoAdmin(admin.ModelAdmin):
    list_display = ('title', 'upload_date')

admin.site.register(Album, AlbumAdmin)
admin.site.register(Photo, PhotoAdmin)
