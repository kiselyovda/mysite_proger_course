from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return HttpResponse('Hello world!')


def test(request):
    return HttpResponse('<h1 style="color: red; border: 4mm ridge rgba(211, 220, 50, .6);"><center>Тестовая надпись</center></h1>')