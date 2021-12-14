from django.contrib import admin

from .models import Sotrudnik
from .models import Qualification
from .models import Licnoe_delo


class Licnoe_deloAdmin (admin.ModelAdmin):
  list_display = ( 'fio', 'number_dela', 'education', 'qualification', 'data_priema', 'dolya', 'hours_worked', 'amount_to_issue')
  list_display_links = ( 'fio', 'number_dela', 'education', 'qualification')
  search_fields = ('fio', 'number_dela', 'education', 'qualification')


admin.site.register(Licnoe_delo, Licnoe_deloAdmin) 
admin.site.register(Qualification)
admin.site.register(Sotrudnik)
