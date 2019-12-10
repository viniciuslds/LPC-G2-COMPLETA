from django.shortcuts import render
from django.urls import reverse
from .models import *
from .forms import *
from .forms import SolicitacaoForm
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.views.generic import TemplateView, FormView, ListView, CreateView
#from django.contrib.auth.forms import UserCreationForm



class HomePageView(TemplateView):
    template_name = 'app_g2/home.html'

def minhasSolicitacoes(request):
    try:
        fun = Funcionario.objects.get(usuario = request.user)
        if fun.cargo.eh_chefe:
            solicitacoes = Solicitacoes.objects.all().order_by('-id')[0:30]
        else:
            solicitacoes = Solicitacoes.objects.filter(solicitante=fun).order_by('-id')[0:30]

    except Exception as identifier:
        return HttpResponse('Você não está logado ao sistema')
    
    return render(request, 'app_g2/minhasSolicitacoes.html', {'solicitacoes': solicitacoes})

def solicita(request, id_solicitacao):
    soli = Solicitacoes.objects.get(pk=id_solicitacao)
    return render(request, 'app_g2/solicita.html', {'soli': soli})


class SolicitacaoView(FormView):
    template_name = 'app_g2/solicitacao.html'
    form_class = SolicitacaoForm

    def form_valid(self, form):
        dados = form.clean()
        pessoa = Funcionario.objects.get(usuario = self.request.user)
        solicitacao = Solicitacoes(solicitante= pessoa, origem=dados['origem'], destino=dados['destino'], qtdPessoas=dados['qtdPessoas'], data=dados['data'])
        solicitacao.save()
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('minhas')

class AtendimentoView(FormView):
    template_name = 'app_g2/atendimento.html'
    form_class = AtendimentoForm


    def form_valid(self, form):
        dados = form.clean()
        solicitacao = dados['solicitacao']
        solicitacao.atendida = True
        solicitacao.save()
        atendimento = Atendimento(veiculo=dados['veiculo'], solicitacao=dados['solicitacao'], motora=dados['motora'],)
        atendimento.save()
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('minhas')

'''class HomePageView(TemplateView):
    template_name = 'app_g2/home.html'''
