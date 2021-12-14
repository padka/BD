from django.contrib import admin

from .models import Qualification
from .models import Licnoe_delo


class Licnoe_deloAdmin (admin.ModelAdmin):
  list_display = ( 'dannie', 'education', 'education')
  list_display_links = ( 'dannie', 'education', 'education')
  search_fields = ('dannie', 'education', 'education')

admin.site.register(Licnoe_delo, Licnoe_deloAdmin) 
admin.site.register(Qualification)

