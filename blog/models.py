from __future__ import unicode_literals # python 2.x 지원용
from django.utils.encoding import python_2_unicode_compatible

from django.db import models
from django.core.urlresolvers import reverse

from tagging.fields import TagField

# Create your models here.

@python_2_unicode_compatible    # Python 2.x 지원용
class Post(models.Model):
    title = models.CharField('TITLE', max_length=50) # 공백과 null 허용
    slug = models.SlugField('SLUG', unique=True, allow_unicode=True, help_text='one word for title alias.') # 매개변수 url 문자열은 url 컬럼에 대한 레이블 문구. 별칭.
    description = models.CharField('DESCRIPTION', max_length=100, blank=True, help_text='simple description text.')
    content = models.TextField('CONTENT')
    create_date = models.DateTimeField('Create Date', auto_now_add=True)
    modify_date = models.DateTimeField('Modify Date', auto_now=True)
    tag = TagField()

    class Meta:
        verbose_name = 'post' # 테이블의 별칭 (단수)
        verbose_name_plural = 'posts' #테이블의 별칭 (복수)
        db_table = 'my_post' # db에 저장되는 테이블 명(미지정시 앱이름_모델클래스명 blog_post 가 됨)
        ordering = ('-modify_date',) # order by 기본 형식('-'가 붙으면 내림차순, !!! ordering은 tuple이나 list형태여야 하므로 마지막 , 을 붙여줘야한다.)

    def __str__(self):
        return self.title

    def get_absolute_url(self): # url을 반환
        return reverse('blog:post_detail', args=(self.slug,)) # 앱명:url name, args는 url 인자 순서
        # url(r'^post/(?P<slug>[-\w]+)/$', PostDV.as_view(), name='post_detail'),

    def get_previous_post(self):
        return self.get_previous_by_modify_date()

    def get_next_post(self):
        return self.get_next_by_modify_date()
