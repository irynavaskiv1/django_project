# Generated by Django 3.2.8 on 2022-01-03 18:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_auto_20210422_1511'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contactus',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='contactus',
            name='phone',
            field=models.TextField(max_length=100, verbose_name='Your phone'),
        ),
    ]