# База данных Начисление зарплаты
from django.db import models
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes.fields import GenericRelation

class Dolznost(models.Model):
    salary_per_hour = models.IntegerField(verbose_name = "Оклад в час")

class Zarplata(models.Model):
    data_viplat = models.DateField(verbose_name = "Дата выплаты")
    hours_worked = models.IntegerField(verbose_name = "Фактически отработанные часы")
    amount_to_issue = models.IntegerField(verbose_name = "Сумма к выдаче")

class Priem_na_raboty(models.Model):
    id_sotr = models.ForeignKey(Dolznost, on_delete=models.CASCADE, verbose_name = "Код_сотрудника")
    data_dismissals = models.DateField(verbose_name = "Дата увольнения")
    dolya = models.IntegerField(verbose_name = "Доля ставки")

class Licnoe_delo(models.Model):
    id_sotr = models.ForeignKey(Priem_na_raboty, on_delete=models.CASCADE, verbose_name = "Код_сотрудника")
    fio =  models.CharField(max_length = 90, verbose_name = "ФИО сотрудника")
    qualification = models.CharField(max_length = 50, verbose_name = "Квалификация")
    education = models.CharField(max_length = 60, verbose_name = "Образование")
    data_priema = models.DateField(verbose_name = "Дата приема")
    number_dela = models.IntegerField(verbose_name = "Номер личного дела")







