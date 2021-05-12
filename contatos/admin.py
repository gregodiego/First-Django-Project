from django.contrib import admin
from contatos.models import Contato, Categoria

class ContatoAdmin(admin.ModelAdmin):
    list_display = ('id','nome','sobrenome', 'telefone', 'email', 'data_criacao','categoria')
    list_display_links = ['nome', 'sobrenome']
    list_per_page = 10
    search_fields = ['id','nome', 'sobrenome']


admin.site.register(Categoria)
admin.site.register(Contato, ContatoAdmin)

