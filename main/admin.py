from django.contrib import admin

# chamar o class de models(main) para aparecer no banco de dados para manipular
from main.models import *

admin.site.register(Item)
