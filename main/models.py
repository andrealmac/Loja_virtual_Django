from django.db import models

# Criar as classes funcoes e carregar tudo para o banco de dados
class Item(models.Model):
    name = models.CharField(max_length=255)
    price = models.IntegerField()
    description = models.CharField(max_length=1000)
    image_url = models.CharField(max_length=512)
    
    #mostrar no banco de dados o que eu cadastrei
    def __str__(self):
        return self.name

#1) python manage.py migrate
#2) python manage.py makemigrations
#3) python manage.py createsuperuser

