#from django.http import HttpResponse
#from django.core.cache import cache
#from django.conf import settings
from rest_framework.decorators import api_view
from rest_framework import status
from rest_framework.response import Response
from django.core.cache import cache
from django.conf import settings
from django.core.cache.backends.base import DEFAULT_TIMEOUT

CACHE_TTL = getattr(settings, 'CACHE_TTL', DEFAULT_TIMEOUT)
from .models import Zarplata

@api_view(['GET'])
def view_zarpl(request):
    zarpl = Zarplata.objects.all()
    results = [zarp.to_json() for zarp in zarpl]
    return Response(results, status=status.HTTP_201_CREATED)


def view_cached_zarpl(request):
    if 'zarp' in cache:
        zarpl = cache.get('zarp')                         
        #return HttpResponse('ФИО сотрудника  ' + zarpl[0]['name']+ ';' + '\n' + 'Квалификация:  ' + zarpl[0]['sotr'] + ';' + '\n' + 'Образование:  ' + zarpl[0]['education']+ ';' + '\n' + 'Фактически отработанные часы:  ' + zarpl[0]['hours_worked'] + ' ч.' + 'Сумма к выдаче:  ' + zarpl[0]['amount_to_issue'] + 'руб.')
        return Response(results, status=status.HTTP_201_CREATED)
    else:
        zarpl = Zarplata.objects.all()
        results = [zarp.to_json() for zarp in zarpl]
        cache.set('zarp', results, timeout=CACHE_TTL)
        #return HttpResponse(results)
        return Response(results, status=status.HTTP_201_CREATED)




