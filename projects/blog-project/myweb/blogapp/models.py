from django.db import models

class Blog(models.Model):
    def __str__(self):
        return self.title

    title = models.CharField(max_length = 200)
    created_date = models.DateTimeField(auto_now_add = True)
    updated_date = models.DateTimeField(auto_now = True)
    body = models.TextField()

    def summary(self):
        return self.body[:20]