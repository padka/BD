from django.db import models

class Sotrudnik(models.Model):
    name = models.CharField(max_length = 90, verbose_name = "ФИО сотрудника")

    def __str__(self):
       return self.name  

    class Meta:
        verbose_name_plural = 'Сотрудник'
        verbose_name = 'Сотрудника'
        ordering = ['name']

class Qualification(models.Model):
    name = models.CharField(max_length = 90, verbose_name = "Квалификация")

    def __str__(self):
        return self.name  

    class Meta:
       verbose_name_plural = 'Квалификация'
       verbose_name = 'Квалификацию'
       ordering = ['name']

class Licnoe_delo(models.Model):

    fio = models.ForeignKey( 'Sotrudnik' , null=True, on_delete = models.PROTECT, verbose_name = "ФИО сотрудника")
    number_dela = models.IntegerField(verbose_name = "Номер личного дела")
    education = models.CharField(max_length = 90, verbose_name = "Образование")
    qualification = models.ForeignKey( 'Qualification' , null=True, on_delete = models.PROTECT, verbose_name = "Квалификация")
    data_priema = models.DateField(verbose_name = "Дата приема")
    dolya = models.IntegerField(verbose_name = "Доля ставки")
    hours_worked = models.IntegerField(verbose_name = "Фактически отработанные часы")
    amount_to_issue = models.IntegerField(verbose_name = "Сумма к выдаче")


    class Meta:
        verbose_name_plural = 'Личное дело'
        verbose_name = 'Личное дело'
        ordering = ['fio']