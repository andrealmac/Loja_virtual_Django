from django.shortcuts import render 

# Vai ser visto pelo usuario
def homepage(request):
    return render(request, template_name='main/home.html')
def itemspage(request):
    return render(request, template_name='main/items.html')