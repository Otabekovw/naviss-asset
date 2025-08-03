from django.db import models


class Partner(models.Model):
    name = models.CharField(max_length=100, verbose_name='Имя партнера')
    image = models.ImageField(upload_to='images/partner/')

    class Meta:
        db_table = 'partner'
        ordering = ['id']

    def __str__(self):
        return self.name


class FAQ(models.Model):
    question = models.CharField(max_length=500, verbose_name='Вопросы')
    answer = models.TextField(max_length=500, verbose_name='Ответы')

    def __str__(self):
        return self.question

    class Meta:
        db_table = 'FAQ'
        ordering = ['id']

class News(models.Model):
    title = models.CharField(max_length=250)
    content = models.TextField(null=True, blank=True)
    date = models.DateTimeField()
    image = models.ImageField(upload_to='images/news/')

    def __str__(self):
        return self.title

    class Meta:
        db_table = 'News'
        ordering = ['id']


class Feedback(models.Model):
    user_name = models.CharField(max_length=250)
    rate = models.IntegerField(default=0.0)
    content = models.TextField()
    date = models.DateTimeField()

    def __str__(self):
        return self.user_name

    class Meta:
        db_table = 'Feedback'
        ordering = ['id']

