from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    return render(request, 'events/index.html')

def search_no_login(request):
    return render(request, 'events/search_no_login.html')
