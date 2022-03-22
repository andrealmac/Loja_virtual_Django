#nome da pagina e onde chama elas
from django.urls import path #caminho que a urls da pasta shop ira usar
from main import views#Chamar o arquivo views da pasta views(main)

urlpatterns = [
    path('home/', views.homepage, name='home'),#caminho e o nome do caminho na pagina
    #path('', include('main.urls')),#chamando a urls da pasta main(APP)
    path('items/', views.itemspage, name='items'),
]