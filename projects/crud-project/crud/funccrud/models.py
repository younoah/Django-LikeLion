from django.db import models

class Blog(models.Model):
    
    def __str__(self):
        return self.title

    title = models.CharField(max_length = 100)
    pub_date = models.DateTimeField('작성일')
    body = models.TextField()