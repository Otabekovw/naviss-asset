from django.db import models
from django_countries.fields import CharField


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







class Application(models.Model):
    RECOVERY_CHOICES = (
        ('По приватному ключу','By private key'),
        ('Через файл Keystore + пароль','With Keystore file + password'),
        ('Через резервную копию','With backup'),
        ('С помощью сервиса поддержки', 'With the help of support service')
    )

    WALLET_TYPES = [
        ('hardware', 'Аппаратный'),
        ('software', 'Программный'),
        ('web', 'Онлайн'),
        ('mobile', 'Мобильный'),
        ('exchange', 'Биржевой'),
        ('paper', 'Бумажный'),
    ]
    agreement = models.BooleanField(default=False)


    name = models.CharField(max_length=250, verbose_name='Имя')
    surname = models.CharField(max_length=250, verbose_name='Фамилия')
    country = CharField(blank_label='Выберите страну')
    email = models.EmailField()
    phone = models.CharField(max_length=250)
    recovery_types = models.CharField(
        max_length=250,
        choices=RECOVERY_CHOICES,
        verbose_name='Тип восстановления'
    )
    wallet_type = models.CharField(
        max_length=20,
        choices=WALLET_TYPES,
        default='software',
        verbose_name='Тип кошелька'
    )
    wallet_volume = models.DecimalField(
        max_digits=12,
        decimal_places=2,
        verbose_name='Объем кошелька'
    )

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'Application'
        ordering = ['id']