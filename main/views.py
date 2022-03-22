from django.shortcuts import render, HttpResponse #HttpResponse para usar o request

# Vai ser visto pelo usuario
def homepage(request):
    #return HttpResponse('<h1>Hello World</h1>') 
    return render(request, template_name='main/home.html')#montar um arquivo em html e referenciando o caminho atraves do template
    
def itemspage(request):
    return render(request, template_name='main/items.html')