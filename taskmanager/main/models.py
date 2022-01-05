from django.db import models


class NewsDB(models.Model):

    title = models.CharField('Назва', max_length=100)
    text = models.TextField('Стаття')
    date = models.DateTimeField('Дата публікації')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Новина'
        verbose_name_plural = 'Новини'
