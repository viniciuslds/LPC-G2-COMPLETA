from django import forms
from .models import *

class SolicitacaoForm(forms.Form):
    origem = forms.CharField(max_length=25)
    destino = forms.CharField(max_length=25)
    qtdPessoas = forms.CharField(max_length=1)
    data = forms.DateTimeField(widget=forms.DateTimeInput())
    

    def clean(self):
        dados = super().clean()
        origem = dados.get('Origem',None)
        destino = dados.get('Destino',None)
        qtdPessoas = dados.get('Quantidade de Pessoas',None)
        data = dados.get('Data e hora',None)
        

        return dados


class AtendimentoForm(forms.Form):
    veiculo = forms.ModelChoiceField(queryset=Veiculos.objects.all())
    solicitacao = forms.ModelChoiceField(queryset=Solicitacoes.objects.filter(atendida = False))
    motora = forms.ModelChoiceField(queryset=Funcionario.objects.filter(cargo__eh_motorista = True))

    def clean(self):
        dados = super().clean()
        veiculo = dados.get('veiculo',None)
        solicitacao = dados.get('solicitacao',None)
        motora = dados.get('motora',None)
        atendida = dados.get('atendida',None)

        return dados