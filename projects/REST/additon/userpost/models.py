from django.db import models
from django.conf import settings

class UserPost(models.Model):
    class Meta:
        ordering = ['id']
    objects = models.Manager() #  class has no objects member 에러 예방
    title = models.CharField(max_length = 50)
    body = models.TextField()
    # 인자설명 : 장고의 유저모델을 사용하고/ 1번 사용자부터 디폴트로 지정/ 유저가 삭제되면 해당 모델의 오브젝트도 삭제
    author = models.ForeignKey(settings.AUTH_USER_MODEL, default = 1, on_delete=models.CASCADE)

# createsuperuser 관리자 2명 만들기 : 그냥 쉽게 유저 2명 추가해보려고 구현
# python manage.py createsuperuser로 서로다른 2명의 관리자 생성
# 1번 유저 : uno
# 2번 유저 : zico