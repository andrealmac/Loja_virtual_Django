from django.shortcuts import render 

#importar os dados dos items no banco de dados
from main.models import Item

# Vai ser visto pelo usuario
def homepage(request):
    return render(request, template_name='main/home.html')
def itemspage(request):
    items = Item.objects.all()
    return render(request, template_name='main/items.html', context={'items':items})

def loginpage(request):
    return render(request, template_name='main/login.html')

def registerpage(request):
    return render(request, template_name='main/registerpage.html')

def logoutpage(request):
    #return render(request, template_name='main/logoutpage.html')
