from django.urls import path
from .views import *

urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path('minhassolicitacoes/', minhasSolicitacoes, name='minhas'),
    path('solicitar/', SolicitacaoView.as_view(), name='solicitar'),
    path('atendimento/', AtendimentoView.as_view(), name='atender'),
    path('solicita/<int:id_solicitacao>', solicita, name='solici'),
    #path('solicitacao/', SolicitacaoView.as_view(), name='solicitacao'),

]