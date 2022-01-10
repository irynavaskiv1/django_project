from django.db import models


class Newstable(models.Model):

    news_id = models.IntegerField('news_id')
    news = models.CharField('news', max_length=100)
    article = models.CharField('article', max_length=100)
    dates = models.CharField('dates', max_length=100)
    times = models.CharField('times', max_length=100)

    def __str__(self):
        return self.news

    class Meta:
        db_table = "Newstable"
