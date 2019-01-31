from django.db import models

# Create your models here.

from django.urls import reverse

class Article(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField(blank=True)
    pub_time = models.DateTimeField(auto_now=True,editable=True)
    summary = models.TextField(blank=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('article-detail',args=[str(self.id)]) 


