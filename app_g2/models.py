from django.db import models
from django.contrib.auth.models import User

class Cargo(models.Model):
    nome = models.CharField(verbose_name='Cargo: ', max_length=60, blank=True, null=True)
    eh_chefe = models.BooleanField(verbose_name='É chefe do departamento de viagens?: ', default=False )
    eh_motorista = models.BooleanField( default=False )
    
    def __str__(self):
        return 'Nome: ' + self.nome

class Departamento(models.Model):
    nome = models.CharField(verbose_name='Departamento: ', max_length=60, blank=True, null=True)
    cod = models.CharField(verbose_name='Codigo do Departamento: ', max_length=60, blank=True, null=True)
    eh_transporte = models.BooleanField( default=False )
    
    
    def __str__(self):
        return 'Nome: ' + self.nome

class Veiculos(models.Model):
    veiculo = models.CharField(verbose_name='Veículo: ', max_length=60, blank=True, null=True)
    placa = models.CharField(verbose_name='Placa: ', max_length=6, blank=True, null=True)
    
    def __str__(self):
        return 'Veiculo: ' + self.veiculo + ' Placa: ' + self.placa

class Funcionario(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user')
    nome = models.CharField(verbose_name='Nome: ', max_length=60, blank=True, null=True)
    matricula = models.CharField(verbose_name='Matricula: ', max_length=14, blank=True, null=True)
    cargo = models.ForeignKey(Cargo, on_delete=models.DO_NOTHING)
    departamento = models.ForeignKey(Departamento, on_delete=models.DO_NOTHING)

    def __str__(self):
        return self.nome

class Solicitacoes(models.Model):
    solicitante = models.ForeignKey(Funcionario, on_delete=models.CASCADE)
    origem = models.CharField(verbose_name='Origem ', max_length=25, blank=True, null=True)
    destino = models.CharField(verbose_name='Destino ', max_length=25, blank=True, null=True)
    qtdPessoas = models.CharField(verbose_name='Quantidade de Pessoas ', max_length=1, blank=True, null=True)
    data = models.DateTimeField(verbose_name='Data e hora ', blank=True, null=True)
    atendida = models.BooleanField( default=False )
    
    def get_absolute_url(self):
        return reverse("solicitacao", kwargs={"solicitacao_id": self.pk})

    def __str__(self):
        return 'O Chefe: {} Solicita um carro para  {} pessoas no dia {} '.format(self.solicitante.nome, self.qtdPessoas,
                                                                                 self.data)

class Atendimento(models.Model):
    veiculo = models.ForeignKey(Veiculos, on_delete=models.DO_NOTHING)
    solicitacao = models.ForeignKey(Solicitacoes, on_delete=models.DO_NOTHING)
    motora = models.ForeignKey(Funcionario, on_delete=models.DO_NOTHING)

    def __str__(self):
        return ('Solicita')