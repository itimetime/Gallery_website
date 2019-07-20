from django.db import models

# Create your models here.


class Blog(models.Model):
    title = models.CharField(default='文章标题',max_length=50)
    date = models.DateTimeField()
    image = models.ImageField(default='default.png',upload_to='images/')
    text = models.TextField(default='正文')

    def __str__(self):
        return self.title

    def short_text(self):
        return self.text[:100] + '...'