from djongo import models

class Sotrudnik(models.Model):
    name = models.CharField(max_length = 90, verbose_name = "ФИО сотрудника")
    hours_worked = models.IntegerField(verbose_name = "Фактически отработанные часы")
    amount_to_issue = models.IntegerField(verbose_name = "Сумма к выдаче")  

    class Meta:
        abstract = True


class Qualification(models.Model):
    name = models.CharField(max_length = 90, verbose_name = "Квалификация")

    def __str__(self):
        return self.name  

    class Meta:
       verbose_name_plural = 'Квалификация'
       verbose_name = 'Квалификацию'
       ordering = ['name']

class Licnoe_delo(models.Model):

    dannie = models.EmbeddedField(model_container=Sotrudnik)
    number_dela = models.IntegerField(verbose_name = "Номер личного дела")
    education = models.CharField(max_length = 90, verbose_name = "Образование")

    class Meta:
        verbose_name_plural = 'Личное дело'
        verbose_name = 'Личное дело'
        ordering = ['number_dela']













