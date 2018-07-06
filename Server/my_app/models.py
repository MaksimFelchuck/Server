# coding=utf-8
from django.db import models

# Create your models here.

class script(models.Model):

    script_name = models.CharField('script_name', max_length= 20, unique = True, db_index = True)
    script = models.TextField()

    def __str__(self):

        return self.script_name





"""""""""
IntegerField - Целое число
TextField - Поле для большого текста
DataTimeField - Поле дата-время
URLField - Поле для URL-адреса, максимум 200 символов 
FileField - Поле загружаемого файла
"""""""""