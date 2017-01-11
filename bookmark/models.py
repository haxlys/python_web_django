from __future__ import unicode_literals # python 2.x 지원용

from django.db import models
from django.utils.encoding import python_2_unicode_compatible

# Create your models here.

@python_2_unicode_compatible    # Python 2.x 지원용
class Bookmark(models.Model):
    title = models.CharField(max_length=100, blank=True, null=True) # 공백과 null 허용
    url = models.URLField('url', unique=True) # 매개변수 url 문자열은 url 컬럼에 대한 레이블 문구. 별칭.

    def __str__(self):
        return self.title
