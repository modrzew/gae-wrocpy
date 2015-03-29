from django.http import HttpResponse


def home(request):
    return HttpResponse('Whooo! It\'s a Django app!')
