from django.db import models


class ContactUs(models.Model):
    """
    Add tables in DB. As usual one model is a one table.
    """
    name = models.CharField('Your name ', max_length=50)
    phone = models.TextField('Your phone', max_length=100)

    def __str__(self):
        return self.phone

    class Meta:
        verbose_name = 'Contact'
        verbose_name_plural = "Contact's"

