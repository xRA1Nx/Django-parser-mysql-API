from django.db import models


class Tag(models.Model):
    name = models.CharField(max_length=20, unique=True)


class Post(models.Model):
    choises = [
        ('oz', 'ozon'),
        ('ya', 'yandex')
    ]
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=500)
    text = models.TextField(max_length=10000)
    date = models.DateField(auto_now=True)
    source = models.CharField(choices=choises, max_length=2)
    tags = models.ManyToManyField(Tag, through='NewsTags')

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['title', 'date'], name='title_date')
        ]



class NewsTags(models.Model):
    tag = models.ForeignKey(Tag, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
