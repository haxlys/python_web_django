from django.contrib import admin
from bookmark.models import Bookmark

# Register your models here.

class BookmarkAdmin(admin.ModelAdmin):
    list_display = ('title', 'url')

# Bookmark 모델을 BookmarkAdmin 클래스에 정의한데로 Admin화면에서 보여진다.
admin.site.register(Bookmark, BookmarkAdmin)
