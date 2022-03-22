from django.shortcuts import render, HttpResponse #HttpResponse para usar o request

# Vai ser visto pelo usuario
def homepage(request):
    return HttpResponse('<h1>Hello World</h1>')