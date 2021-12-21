from django.conf.urls import url
from .views import view_cached_zarpl
from .views import view_zarpl
 
urlpatterns = [
    url(r'^$', view_zarpl),
    url(r'^delo', view_cached_zarpl),
]