from django.db import models
from django.conf import settings

# Create your models here.
class Movies(models.Model):
    like_users = models.ManyToManyField(settings.AUTH_USER_MODEL,related_name='like_movies')
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE) 
    title = models.CharField(max_length=20)
    description = models.TextField()

    def __str__(self):
        return f'{self.id}번째글 - {self.title}'

class Comment(models.Model):
    content = models.CharField(max_length=100)
    movie = models.ForeignKey(Movies, on_delete=models.CASCADE) 
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE) 

    def __ser__(self):
        return self.content
