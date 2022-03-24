from django.shortcuts import render, redirect #import redirect para enviar os POST

#importar os dados dos items no banco de dados
from main.models import Item

from django.contrib.auth import authenticate, login, logout #para realizar os metodos de login
from django.contrib.auth.forms import UserChangeForm

# Vai ser visto pelo usuario
def homepage(request):
    return render(request, template_name='main/home.html')
def itemspage(request):
    items = Item.objects.all()
    return render(request, template_name='main/items.html', context={'items':items})

def loginpage(request):
    if request.method == 'GET':
        return render(request, template_name='main/login.html')
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username = username, password=password)
        #Saber se os campos tem algo digitado
        if user is not None:
            return redirect('items')
        #Caso esteja vazio
        else:
            return redirect('login')

def registerpage(request):
    if request.method == 'GET':
        return render(request, template_name='main/register.html')
    if request.method == 'POST':
        form = UserChangeForm(request.POST)   
        if form.is_valid():#como se fosse salvar um commit
            form.save()
            #autenticacao do login e senha
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(username = username, password=password)
            return redirect('home')
        else:
            return redirect('register')
        
    return redirect('register')

def logoutpage(request):
    pass
    #return render(request, template_name='main/logout.html')
