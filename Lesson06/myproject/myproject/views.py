# from django.http import HttpResponse
from django.shortcuts import render


def homepage(request):
    return render(request, 'home.html')
    # return HttpResponse('This is my Homepage! Welcome!')


def about(request):
    return render(request, 'about.html')
    # return HttpResponse('This is my About Page!')
