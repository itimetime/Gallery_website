# Generated by Django 2.2.3 on 2019-07-20 07:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gallery', '0002_auto_20190720_1017'),
    ]

    operations = [
        migrations.AlterField(
            model_name='gallery',
            name='G_images',
            field=models.ImageField(default='default.png', upload_to='images/', verbose_name='添加图片'),
        ),
        migrations.AlterField(
            model_name='gallery',
            name='description',
            field=models.CharField(default='在这里写作品的简介', max_length=150, verbose_name='添加描述'),
        ),
        migrations.AlterField(
            model_name='gallery',
            name='title',
            field=models.CharField(default='作品标题', max_length=150, verbose_name='添加标题'),
        ),
    ]
