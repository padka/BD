from django.urls import path
from .views import index, by_rubric, Licnoe_deloCreateView
urlpatterns = [
   path('add/', Licnoe_deloCreateView.as_view(), name='add'),  
   path('<int:rubric_id>/',by_rubric, name='by_rubric'),
   path('', index, name='index'),
] 