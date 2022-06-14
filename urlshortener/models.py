from django.db import models
from .utils import create_shortened_url
# Create your models here.

class Shortener(models.Model):
    '''
    created : URL이 추가된 날짜와 시간
    times_followed : 짧은 링크를 팔로우한 쵯수
    origin_url : 원본 URL
    short_url : 짧아진 URL 
    '''
    created = models.DateTimeField(auto_now_add=True)
    times_followed = models.PositiveIntegerField(default=0)
    origin_url = models.URLField()
    short_url = models.CharField(max_length=15, unique=True, blank=True)

    def __str__(self):
        return f'{self.origin_url} to {self.short_url}'

    def save(self, *args, **kwargs):

        # 만약 short url이 지정되지 않았다면
        if not self.short_url:
            # 저장중인 model instance를 전달
            self.short_url = create_shortened_url(self)

        super().save(*args, **kwargs)