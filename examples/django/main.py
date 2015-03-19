import os

from django.core.handlers.wsgi import WSGIHandler
from django.http import HttpResponse
from django.core.management import setup_environ
from wrocpy import settings

setup_environ(settings)

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "wrocpy.settings")


def index(request):
    return HttpResponse('Hello, world.')

application = WSGIHandler()
