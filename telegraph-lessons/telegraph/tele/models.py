from django.db import models
from django.urls import reverse


class Article(models.Model):
    title = models.CharField(max_length=200)
    body = models.TextField()

    def get_absolute_url(self):
        return reverse('showArticle', kwargs={'pk': self.pk})

class Images(models.Model):
    post = models.ForeignKey(Article, default=None, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='media/img',
                              verbose_name='Image')