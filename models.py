from django.db import models

class Bb(models.Model):
    fio = models.CharField(max_length = 90)
    number_dela = models.IntegerField()
    education = models.CharField(max_length = 90)
    price = models.IntegerField()

