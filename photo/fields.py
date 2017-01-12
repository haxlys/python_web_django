from django.db.models.fields.files import ImageField, ImageFieldFile
from PIL import Image

import os

def _add_thumb(s): # thumb name 명 제작 함수
    parts = s.split(".")
    parts.insert(-1, "thumb") # filename.jpg -> filename.thumb.jpg 형식으로 변한
    if parts[-1].lower() not in ['jpeg','jpg']: # 확장자 jpg로 변환
        parts[-1] = 'jpg'
    return ".".join(parts)

class ThumbnailImageFieldFile(ImageFieldFile): # ImageFieldFile 파일을 직접 쓰고 지우는 역할
    # 파일은 path와 url 경로를 제공해야 한다. 아래 두 함수가 그 역할을 담당한다.
    def _get_thumb_path(self): # 파일 경로 추가
        return _add_thumb(self.path)
    thumb_path = property(_get_thumb_path)

    def _get_thumb_url(self): # 파일 URL 추가
        return _add_thumb(self.url)
    thumb_url = property(_get_thumb_url)

    def save(self, name, content, save=True): # 파일 저장 함수
        super(ThumbnailImageFieldFile, self).save(name, content, save) # 이미지 저장
        img = Image.open(self.path) # 설치한 PIL 패키지를 이용한 썸네일 생성

        size = (128,128) # 가로 세로
        img.thumbnail(size, Image.ANTIALIAS)
        background = Image.new('RGBA', size, (255, 255, 255, 0)) #하얀색 불투명한 배경을 만듬
        background.paste(img, (int((size[0] - img.size[0]) / 2), int((size[1] - img.size[1]) / 2) )) # 배경과 사진을 붙임
        background.save(self.thumb_path, 'JPEG') # 이미지 생성

    def delete(self, save=True): # 삭제 함수
        if os.path.exists(self.thumb_path):
            os.remove(self.thumb_path)
        super(ThumbnailImageFieldFile, self).delete(save)

class ThumbnailImageField(ImageField): # 필드 역할을 하는 클래스
    attr_class = ThumbnailImageFieldFile # File처리 하는 클래스를 정의해야 한다.

    def __init__(self, thumb_width=128, thumb_height=128, *args, **kwargs): # 썸네일 크기 지정
        self.thumb_width = thumb_width
        self.thumb_height = thumb_height
        super(ThumbnailImageField, self).__init__(*args, **kwargs)
