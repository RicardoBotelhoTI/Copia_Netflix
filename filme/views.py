from django.shortcuts import render, redirect, reverse
from .models import Filme, Usuario
from django.views.generic import TemplateView, ListView, DetailView, FormView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin
from .forms import CriarContaForma, FormHomePage


class HomePage(FormView):
	template_name = 'homepage.html'
	form_class = FormHomePage

	def get(self, request, *args, **kwargs):
		if request.user.is_authenticated:  # usuario esta autenticado:
			# redireciona para a homefilmes
			return redirect('filme:homefilmes')
		else:
			return super().get(request, *args, **kwargs)  # redireciona para a homepage

	def get_success_url(self):
		email = self.request.POST.get('email')
		usuarios = Usuario.objects.filter(email=email)
		if usuarios:
			return reverse('filme:login')
		else:
			return reverse('filme:criarconta')



class HomeFilmes(LoginRequiredMixin, ListView):
	template_name = 'homefilmes.html'
	model = Filme
	# object_list - Lista de itens do modelo


class DetalhesFilme(LoginRequiredMixin, DetailView):
	template_name = 'detalhesfilme.html'
	model = Filme
	# object - 1 item do nosso modelo


	def get(self, request, *args, **kwargs):
		# contabilizar visualização
		filme = self.get_object()
		filme.visualizacoes += 1
		filme.save()
		usuario = request.user
		usuario.filmes_vistos.add(filme)
		return super().get(request, *args, **kwargs) # Redireciona para a URL final


	def get_context_data(self, **kwargs):
		context = super(DetalhesFilme, self).get_context_data(**kwargs)
		# filtrar a minha tabela de filmes pegando os filmes cuja categoria é igual a categoria do filme da página (object)
		# self.get_object()
		filmes_relacionados = Filme.objects.filter(categoria=self.get_object().categoria)[0:5]
		context["filmes_relacionados"] = filmes_relacionados
		return context


class PesquisaFilme(LoginRequiredMixin, ListView):
	template_name = 'pesquisa.html'
	model = Filme

	# object_list
	def get_queryset(self):
		termo_pesquisa = self.request.GET.get('query')
		if termo_pesquisa:
			object_list = Filme.objects.filter(titulo__icontains=termo_pesquisa)
			return object_list
		else:
			return None


class EditarPerfil(LoginRequiredMixin, UpdateView):
	template_name = 'editarperfil.html'
	model = Usuario
	fields = ['first_name', 'last_name', 'email']

	def get_success_url(self):
		return reverse('filme:homefilmes')


class CriarConta(FormView):
	template_name = 'criarconta.html'
	form_class = CriarContaForma

	def form_valid(self, form): # Validação para salvar no BD
		form.save()
		return super().form_valid(form)

	def get_success_url(self):
		return reverse('filme:login') # função pede como resposta um link (sempre usar reverse ao inves de redirect)