from csv import list_dialects
from django.contrib import admin

from site_institucional.forms import ProdutoForm

from .models import FormContato, Inicio, Produto, Mensagem, Depoimento, Contato

# Register your models here.
class InicioAdmin(admin.ModelAdmin):
    list_display = ('id', 'titulo')

admin.site.register(Inicio, InicioAdmin)

class ProdutoFormAdmin(admin.ModelAdmin):
    form = ProdutoForm
admin.site.register(Produto, ProdutoFormAdmin)
admin.site.register(Mensagem)
admin.site.register(Depoimento)
admin.site.register(Contato)

class FormContatoAdmin(admin.ModelAdmin):
    list_display = ('id', 'nome')
    

admin.site.register(FormContato, FormContatoAdmin)