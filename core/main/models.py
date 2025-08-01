from django.db import models

class Partners(models.Model):
    img = models.ImageField(verbose_name="Партнеры", upload_to="partners/")

    def __str__(self):
        return str(self.img)

class News(models.Model):
    title = models.CharField(verbose_name="Название", max_length=255)
    img = models.ImageField(verbose_name="Изображение")
    date = models.DateField(verbose_name="Дата")
    hours = models.IntegerField(verbose_name="Часы")

    def __str__(self):
        return self.title

class Contacts(models.Model):
    name = models.CharField(verbose_name="Имя", max_length=100)
    surname = models.CharField(verbose_name="Фамилия", max_length=100)
    country = models.CharField(verbose_name="Страна", max_length=100)
    email = models.EmailField(verbose_name="E-mail")
    phone = models.BigIntegerField(verbose_name="Номер телефона")

    def __str__(self):
        return f"{self.name} {self.surname}"

class Applications(models.Model):
    name = models.CharField(verbose_name="Имя", max_length=100)
    surname = models.CharField(verbose_name="Фамилия", max_length=100)
    country = models.CharField(verbose_name="Страна", max_length=100)
    email = models.EmailField(verbose_name="E-mail")
    phone = models.BigIntegerField(verbose_name="Номер телефона")

    def __str__(self):
        return f"{self.name} {self.surname}"

class Review(models.Model):
    name = models.CharField(verbose_name="Имя", max_length=100)
    comment = models.TextField(verbose_name="Комменты")
    rating = models.DecimalField(verbose_name="Звездочки", max_digits=2, decimal_places=1, default=5.0)

    def __str__(self):
        return f"{self.name} - {self.rating}"

class Detailednews(models.Model):
    title = models.CharField(verbose_name="Название", max_length=255)
    img = models.ImageField(verbose_name="Изображение")
    date = models.DateField(verbose_name="Дата")
    hours = models.IntegerField(verbose_name="Часы")
    text = models.TextField(verbose_name="Текст")

    def __str__(self):
        return self.title
