from django.db import models


class News(models.Model):

    title = models.CharField('Name', max_length=100)
    text = models.TextField('Article', max_length=100)
    date = models.DateTimeField('Date', max_length=100)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'News'
        verbose_name_plural = 'All News'
