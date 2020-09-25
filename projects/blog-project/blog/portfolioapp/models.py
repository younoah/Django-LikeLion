from django.db import models

class Portfolio(models.Model):

    def __str__(self):
        return self.title

    title = models.CharField(max_length = 200)
    image = models.ImageField(upload_to = 'images/')
    description = models.TextField()