import pandas as pd
import csv
from django.db import models
from datetime import *
from django.utils import timezone

    
'''Banco de dados do Aluno'''
class Aluno(models.Model):
    nome = models.CharField('Nome', max_length=100)
    sobrenome = models.CharField('Sobrenome', max_length=100)
    serie = models.IntegerField('Qual série estuda')
    
    def __str__(self):
        return self.nome

'''Banco de Dados da catalogação do livro'''
class Catalogacao(models.Model):
    nome_book = models.CharField('Nome do Livro', max_length=100)
    aut = models.CharField('Nome do autor', max_length=100)
    editora = models.CharField('Editora', max_length=100)
    ano = models.IntegerField('Ano de publicação')
    
    def __str__(self):
        return self.nome_book

'''Indicações'''
    
'''Banco de dados do empréstimo do livro '''
class Emprestimo(models.Model):
    nome_aluno = models.CharField('Nome do aluno', max_length=100)
    nome_livro = models.CharField('Nome do livro', max_length=100)
    autor = models.CharField(max_length=100, verbose_name='Autor do livro')
    ano = models.DecimalField(decimal_places=2, max_digits=8, verbose_name='Ano de publicação')
    data_emprestimo = models.DateTimeField('Data de empréstimo')
    data_devol = models.DateField('Data de devolução')

    @staticmethod
    def upload_emprestimos(file):
        # Lê o arquivo enviado pelo usuário com pandas
        emprestimos = pd.read_excel(file)

        # Converte as colunas do pandas para uma lista de dicionários de empréstimos
        emprestimos_list = emprestimos.to_dict('records')

        # Cria objetos de empréstimo a partir dos dados da lista de dicionários
        for emprestimo_data in emprestimos_list:
            emprestimo = Emprestimo.objects.create(
                nome_livro=emprestimo_data['titulo'],
                data_emprestimo=emprestimo_data['data_emprestimo'],
                data_devol=emprestimo_data['data_devolucao']
            )
            emprestimo.save()
            
    hoje = datetime.today().date()
    def atraso(self): 
        hoje = datetime.today().date()
        atraso = hoje - self.data_devol 
        
        if atraso.days > 0:
            for c in range (atraso.days):
                c += atraso.days
                return f'Atrasado {c} dias'
            
            return 'Atrasado'
        
        else:
            return 'Aluno em dias'
    

    
    def __str__(self):
        return self.nome_aluno
    
    @staticmethod
    def import_from_csv(csv_file):
        with open(csv_file, 'r') as file:
            reader = csv.reader(file)
            for row in reader:
                try:
                    livro = Catalogacao.objects.get(titulo=row[0])
                    usuario = Aluno.objects.get(nome=row[1])
                    Emprestimo.objects.create(livro=livro, usuario=usuario)
                except (Catalogacao.DoesNotExist, Aluno.DoesNotExist):
                    pass


class Loan(models.Model):
    livro = models.ForeignKey(Catalogacao, on_delete=models.CASCADE)
    usuario = models.ForeignKey(Aluno, on_delete=models.CASCADE)
    date = models.DateTimeField(default=timezone.now)
    return_date = models.DateTimeField(blank=True, null=True)

    def __str__(self):
        return f"{self.book} - {self.user}"
    
class Statistics(models.Model):
    book = models.ForeignKey(Catalogacao, on_delete=models.CASCADE)
    user = models.ForeignKey(Aluno, on_delete=models.CASCADE)
    loan_count = models.IntegerField(default=0)
    last_loan_date = models.DateTimeField(blank=True, null=True)

    def __str__(self):
        return f"{self.book} - {self.user} - {self.loan_count} loans"

    @classmethod
    def generate_statistics(cls):
        for book in Catalogacao.objects.all():
            for user in Aluno.objects.all():
                loan_count = Loan.objects.filter(book=book, user=user).count()
                last_loan = Loan.objects.filter(book=book, user=user).order_by('-loan_date').first()
                if last_loan is None:
                    last_loan_date = None
                else:
                    last_loan_date = last_loan.loan_date
                stat, created = cls.objects.get_or_create(book=book, user=user)
                stat.loan_count = loan_count
                stat.last_loan_date = last_loan_date
                stat.save()