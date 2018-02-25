from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class Article(models.Model):
    title = models.CharField(max_length=100)
    slug =  models.SlugField()
    body =  models.TextField()
    date =  models.DateTimeField(auto_now_add=True)
    thumb = models.ImageField(default='default1.jpg',blank=True)
    author = models.ForeignKey(User,on_delete=False,default=None)

    def __str__(self):
        return  self.title

    # show only 50 char
    def snippet(self):
        return self.body[:50]+"..."


