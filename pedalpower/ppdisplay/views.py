from django.shortcuts import render
from django.template import *

from django.http import HttpResponse


def index(request):
    return render(request, 'ppdisplay/index.html', {})