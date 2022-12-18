from django.db import models

# Create your models here.

class MyTable(models.Model):
    name=models.CharField(max_length=100)
    email=models.EmailField(max_length=100)
    age=models.CharField(max_length=100)
    date=models.DateField(auto_now=True)#автоматическое обновление даты

    def user_data(self):
        return f'Имя пользователя: {self.name}, почта: {self.email}, возраст: {self.age}'

class divans(models.Model):
    name=models.CharField(max_length=100, verbose_name="Название")
    color=models.CharField(max_length=100, verbose_name="Цвет")
    cost=models.PositiveSmallIntegerField(verbose_name="Цена")
    image=models.ImageField(upload_to="myapp/static", blank=True)
class tables(models.Model):
    name=models.CharField(max_length=100, verbose_name="Название")
    color=models.CharField(max_length=100, verbose_name="Цвет")
    cost=models.PositiveSmallIntegerField(verbose_name="Цена")




