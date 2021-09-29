from django.db import models


class Articles(models.Model):
    title = models.CharField('Назва', max_length=30, default='Цікаве про село')
    anons = models.CharField('Анонс', max_length=100, default='Анонс про подію')
    text = models.TextField('Стаття')
    date = models.DateTimeField('Дата публікації')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Новина'
        verbose_name_plural = 'Новини'
