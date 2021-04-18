from django.db import models


class ContactUs(models.Model):
    name = models.CharField('Your name ', max_length=50)
    phone = models.CharField('Your phone', max_length=12)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Contact'
        verbose_name_plural = "Contact's"

