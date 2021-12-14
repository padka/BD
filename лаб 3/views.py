from django.http import HttpResponse
from .models import Sotrudnik, Qualification, Licnoe_delo
from django.template import loader
from django.shortcuts import render
from django.urls import reverse_lazy

from django.views.generic.edit import CreateView
from .forms import Licnoe_deloForm


def index(request):
   template =  loader.get_template('bboard/index.html')
   licn = Licnoe_delo.objects.all()
   qualif = Qualification.objects.all()
   sotr = Sotrudnik.objects.all()  
   context = {'licn':licn,'sotr':sotr, 'qualif':qualif}
   return HttpResponse(template.render(context,request))

def by_rubric(request, rubric_id):
  licn = Licnoe_delo.objects.get(fio=rubric_id)
  current_sotr = Sotrudnik.objects.get(pk=rubric_id)
  qualif = Qualification.objects.all()
  sotr = Sotrudnik.objects.all()  
  context = {'licn':licn,'sotr':sotr, 'current_sotr':current_sotr, 'qualif':qualif}
  return render(request, 'bboard/by_rubric.html', context)

class Licnoe_deloCreateView(CreateView):
  template_name= 'bboard/create.html'
  form_class = Licnoe_deloForm
  success_url = reverse_lazy('index')

  
  def get_context_data(self, **kwargs):
    context = super().get_context_data(**kwargs)
    context['sotr'] = Sotrudnik.objects.all()   
    return context
