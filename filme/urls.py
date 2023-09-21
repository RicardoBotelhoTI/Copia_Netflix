from django.urls import path
from . import views as v

app_name = 'filme'

urlpatterns = [
    path('', v.HomePage.as_view(), name='homepage'),
    path('filmes/', v.HomeFilmes.as_view(), name='homefilmes'),
    path('filmes/<int:pk>', v.DetalhesFilme.as_view(), name='detalhesfilme'),
    path('pesquisa/', v.PesquisaFilme.as_view(), name='pesquisafilme')
]