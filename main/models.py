from django.db import models
#python manage.py migrate
# Criar as classes funcoes e carregar tudo para o banco de dados
class Item(models.Model):
    name = models.CharField(max_length=255)
    price = models.IntegerField()
    description = models.CharField(max_length=1000)
    image_url = models.CharField(max_length=512)
    