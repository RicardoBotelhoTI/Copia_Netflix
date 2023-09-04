from django.shortcuts import render
from .models import Filme
from django.views.generic import TemplateView, ListView, DetailView


"""def homepage(request):
	return render(request, 'homepage.html')"""

class HomePage(TemplateView):
	template_name = 'homepage.html'



"""def homefilmes(request):
	lista_filmes = Filme.objects.all()
	return render(request, 'homefilmes.html', {'lista_filmes': lista_filmes})"""

class HomeFilmes(ListView):
	template_name = 'homefilmes.html'
	model = Filme
	# object_list - Lista de itens do modelo


class DetalhesFilme(DetailView):
	template_name = 'detalhesfilme.html'
	model = Filme
	# object - 1 item do nosso modelo