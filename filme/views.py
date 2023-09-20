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


	def get(self, request, *args, **kwargs):
		# Descobrir qual o filme ele está acessando
		filme = self.get_object()
		filme.visualizacoes += 1
		filme.save()
		return super().get(request, *args, **kwargs) # Redireciona para a URL final


	def get_context_data(self, **kwargs):
		context = super(DetalhesFilme, self).get_context_data(**kwargs)
		# filtrar a minha tabela de filmes pegando os filmes cuja categoria é igual a categoria do filme da página (object)
		# self.get_object()
		filmes_relacionados = Filme.objects.filter(categoria=self.get_object().categoria)[0:5]
		context["filmes_relacionados"] = filmes_relacionados
		return context