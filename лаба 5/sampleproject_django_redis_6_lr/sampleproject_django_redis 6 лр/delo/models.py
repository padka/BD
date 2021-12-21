from django.db import models

class Zarplata(models.Model):
 
 name = models.CharField(max_length = 90, verbose_name = "ФИО сотрудника")
 sotr = models.CharField(max_length = 90, verbose_name = "Квалификация")
 education = models.CharField(max_length = 80, verbose_name = "Образование")
 hours_worked = models.CharField(max_length = 30, verbose_name = "Фактически отработанные часы")
 amount_to_issue = models.CharField(max_length = 20, verbose_name = "Сумма к выдаче")
 
 def __unicode__(self):
     return self.name

 def to_json(self):
     return {
         'name' : self.name,
         'sotr': self.sotr,
         'education': self.education,
         'hours_worked': self.hours_worked,
         'amount_to_issue': self.amount_to_issue,
           
  }

 class Meta:
   verbose_name_plural = 'Зарплата'
   verbose_name='Зарплату'
   ordering = ['name']