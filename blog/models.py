from django.db import models
from django.conf import settings
from django.utils import timezone


# Create your models here.
class Post(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=100, verbose_name='Заголовок')
    text = models.TextField(verbose_name='Текст поста')
    create_date = models.DateTimeField(default=timezone.now, verbose_name='Дата создания')
    published_date = models.DateTimeField(blank=True, null=True, verbose_name='Дата публикации')

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    class Meta:
        verbose_name_plural = 'Посты'
        verbose_name = 'Пост'
        ordering = ['-published_date']

    def __str__(self):
        return self.title
