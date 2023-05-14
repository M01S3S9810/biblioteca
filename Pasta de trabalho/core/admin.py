from django.contrib import admin

# Register your models here.
from.models import Aluno, Emprestimo, Catalogacao

    
class EstudanteAdmin(admin.ModelAdmin):
    list_display = ('nome', 'sobrenome', 'serie') 

class EmprestimoAdmin(admin.ModelAdmin):
    list_display = ('nome_aluno','nome_livro','autor', 'ano', 'data_emprestimo', 'data_devol', 'atraso')
    
class CatalogacaoAdmin(admin.ModelAdmin):
    list_display = ('nome_book', 'aut', 'editora', 'ano')
    
 

admin.site.register(Aluno, EstudanteAdmin)
admin.site.register(Emprestimo, EmprestimoAdmin)
admin.site.register(Catalogacao, CatalogacaoAdmin)