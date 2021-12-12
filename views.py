from django.http import HttpResponse
from .models import Bb

def index(request):
    s = 'Список сотрудников:\r\n\r\n\r\n'
    for bb in Bb.objects.all():
        s += 'Сотрудник:  ' + bb.fio + '\r\n' + 'Образование:  ' + bb.education + '\r\n\r\n';
    return HttpResponse(s, content_type='text/plain; charset=utf-8')