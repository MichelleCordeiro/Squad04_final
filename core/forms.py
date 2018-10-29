from django import forms
from django.core.mail import send_mail
from django.conf import settings
from . import views
#form .models import 

class ContactForm(forms.Form):
	name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Seu nome', 'data-rule':'minlen:4', 'data-msg': 'Por favor, insira pelo menos 4 caracteres.'}))
	email = forms.CharField(widget=forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Seu e-mail', 'data-rule':'email', 'data-msg': 'Por favor, insira um email válido.'}))
	sbjct = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Assunto', 'data-rule':'minlen:4', 'data-msg': 'Por favor, insira pelo menos 8 caracteres no assunto.'}))
	msg = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Mensagem', 'rows': '5', 'data-rule':'required', 'data-msg': 'Por favor, insira sua mensagem.'}))

	def send_mail(self):
		message = ' Nome: %(nome)s\n E-mail: %(email)s\n \n %(message)s'
		subject = self.cleaned_data['sbjct']
		context = {
			'nome' : self.cleaned_data['name'],
			'email': self.cleaned_data['email'],
			'message' :self.cleaned_data['msg'],
		}
		message = message % context
		send_mail(subject, message, settings.DEFAULT_FROM_EMAIL, [settings.CONTACT_EMAIL], fail_silently=False)

class OrcamentoForm(forms.Form):
	name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Seu nome', 'data-rule':'minlen:4', 'data-msg': 'Por favor, insira seu nome.'}))
	email = forms.CharField(widget=forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Seu e-mail', 'data-rule':'email', 'data-msg': 'Por favor, insira um email válido.'}))
	campo = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Campo', 'data-rule':'minlen:4', 'data-msg': 'Por favor, insira pelo menos 4 caracteres.'}))
	quant_kW = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Quantidade de kW consumido', 'data-rule':'minlen:4', 'data-msg': 'Por favor, insira a quantidade.'}))
	obs = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Outras Observações', 'rows': '5', 'data-rule':'required', 'data-msg': 'Por favor, insira suas observações.'}))

	def send_mail(self):
		message = ' Nome: %(nome)s\n E-mail: %(email)s\n \n %(message)s'
		subject = self.cleaned_data['sbjct']
		context = {
			'nome' : self.cleaned_data['name'],
			'email': self.cleaned_data['email'],
			'message' :self.cleaned_data['msg'],
		}
		message = message % context
		send_mail(subject, message, settings.DEFAULT_FROM_EMAIL, [settings.CONTACT_EMAIL], fail_silently=False)

		