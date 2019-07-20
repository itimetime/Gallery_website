from django.db import models

# Create your models here.

class Gallery(models.Model):
    description = models.CharField(verbose_name='添加描述',default='在这里写作品的简介',max_length=150)
    G_images = models.ImageField(verbose_name='添加图片',default='default.png',upload_to='images/')
    title = models.CharField(verbose_name='添加标题',default='作品标题',max_length=150)
    def __str__(self):
        return self.title
