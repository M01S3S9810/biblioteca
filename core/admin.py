from django.contrib import admin
from .models import Emprestimo, Statistics
from import_export import resources
from import_export.admin import ImportExportModelAdmin
from .models import Emprestimo

# Register your models here.
from.models import Aluno, Emprestimo, Catalogacao

class EstudanteAdmin(admin.ModelAdmin):
    list_display = ('nome', 'sobrenome', 'serie') 

class EmprestimoResource(resources.ModelResource):
    
    class Meta:
        model = Aluno
        
@admin.register(Emprestimo)
class EmprestimoAdmin(ImportExportModelAdmin):
    resource_classes = [EmprestimoResource]
    list_display = ('nome_aluno','nome_livro','autor', 'ano', 'data_emprestimo', 'data_devol', 'atraso')
            
class CatalogacaoAdmin(admin.ModelAdmin):
    list_display = ('nome_book', 'aut', 'editora')

@admin.register(Statistics)
class StatisticsAdmin(admin.ModelAdmin):
    list_display = ('book', 'user', 'loan_count', 'last_loan_date')
    list_filter = ('book', 'user')

    def get_queryset(self, request):
        qs = super().get_queryset(request)
        return qs.select_related('book', 'user')

    def has_add_permission(self, request):
        return False

    def has_delete_permission(self, request, obj=None):
        return False

admin.site.register(Aluno, EstudanteAdmin)
admin.site.register(Catalogacao, CatalogacaoAdmin)
