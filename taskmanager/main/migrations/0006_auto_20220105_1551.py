# Generated by Django 3.2.8 on 2022-01-05 15:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0005_articles'),
    ]

    operations = [
        migrations.DeleteModel(
            name='ContactUs',
        ),
        migrations.AlterField(
            model_name='articles',
            name='title',
            field=models.CharField(max_length=100, verbose_name='Назва'),
        ),
    ]
