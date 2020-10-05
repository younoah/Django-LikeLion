from django.db import models

class Post(models.Model):
    objects = models.Manager() #  class has no objects member 에러 예방
    title = models.CharField(max_length = 50)
    body = models.TextField()
