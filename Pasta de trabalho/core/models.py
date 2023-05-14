from django.db import models
from datetime import *

'''Banco de dados do Produto '''


'''Banco de dados do Aluno'''
class Aluno(models.Model):
    nome = models.CharField('Nome', max_length=100)
    sobrenome = models.CharField('Sobrenome', max_length=100)
    serie = models.IntegerField('Qual série estuda')
    
    def __str__(self):
        return self.nome
    
'''Banco de dados do empréstimo do livro '''
class Emprestimo(models.Model):
    nome_aluno = models.CharField('Nome do aluno', max_length=100)
    nome_livro = models.CharField('Nome do livro', max_length=100)
    autor = models.CharField(max_length=100, verbose_name='Autor do livro')
    ano = models.DecimalField(decimal_places=2, max_digits=8, verbose_name='Ano de publicação')
    data_emprestimo = models.DateTimeField('Data de empréstimo')
    data_devol = models.DateField('Data de devolução')
    
    hoje = datetime.today().date()
    def atraso(self): 
        hoje = datetime.today().date()
        atraso = hoje - self.data_devol 
        
        if atraso.days > 0:
            return 'Atraso'
        
        else:
            return 'Em dia'

    
    def __str__(self):
        return self.nome_aluno

'''Banco de Dados da catalogação do livro'''
class Catalogacao(models.Model):
    nome_book = models.CharField('Nome do Livro', max_length=100)
    aut = models.CharField('Nome do autor', max_length=100)
    editora = models.CharField('Editora', max_length=100)
    ano = models.IntegerField('Ano de publicação')
    
    
    def __str__(self):
        return self.nome_book
    