# Generated by Django 3.1.5 on 2021-01-16 05:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_auto_20210115_2346'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='image_header',
            field=models.ImageField(upload_to='posts/photos', verbose_name='Imagen del Post'),
        ),
    ]