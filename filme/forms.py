from django.contrib.auth.forms import UserCreationForm
from .models import Usuario
from django import forms


class FormHomePage(forms.Form):
	email = forms.EmailField(label=False)


class CriarContaForma(UserCreationForm):
	email = forms.EmailField() # Email obrigatorio

	class Meta:
		model = Usuario
		fields = ('username', 'email', 'password1', 'password2')