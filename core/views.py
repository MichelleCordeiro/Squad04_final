from django.shortcuts import render
from django.http import HttpResponse
from .models import Slideshow, Quem_Somos, Servicos
from .forms import ContactForm, OrcamentoForm

# Create your views here.

def index(request):
	slideshow = Slideshow.objects.all()
	quemsomos = Quem_Somos.objects.all()
	servicos = Servicos.objects.all()

	context={
		'slideshow':slideshow,
		'quemsomos':quemsomos,
		'servicos':servicos,
	}

	if request.method == 'POST':
		form = ContactForm(request.POST)
		if form.is_valid():
			context['is valid'] = True
			form.send_mail()
			form = ContactForm()
	else:
		form = ContactForm()

	context['form'] = form
	return render(request, 'index.html', context)