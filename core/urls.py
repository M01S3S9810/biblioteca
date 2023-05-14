from django.urls import path

from .views import index, contato, aluno


urlpatterns = [
    path('', index, name='index'), 
    path('contato', contato, name='contato'),
    path('aluno/<int:pk>', aluno, name='aluno'),

]
