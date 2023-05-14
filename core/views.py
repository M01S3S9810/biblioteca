from django.shortcuts import render
from .models import Aluno
from django.shortcuts import get_object_or_404

def index(request):
    alunos = Aluno.objects.all()
    serie = Aluno.objects.all()
    context = {
    'curso': 'Biblioteca - Tristão de Barros', 
    'outro': 'Gerencie a sua biblioteca!',
    'alunos': alunos,
    'series': serie
    }
    return render(request, 'index.html', context)
def contato(request):
    return render(request, 'contato.html')

def aluno(request, pk):
    # alun = Aluno.objects.get(id=pk)
    
    alun = get_object_or_404(Aluno, id=pk)
    context = {
        'aluno': alun
    }
    return render(request, 'aluno.html', context)

def error404(request, exception):
    return render(request, '404.html')