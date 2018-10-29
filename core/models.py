from django.db import models

# Create your models here.

class Slideshow(models.Model):
	titulo = models.CharField('Titulo inicial', max_length = 100)
	descricao = models.CharField('Descrição', max_length = 200)
	imagem = models.ImageField('Imagem', upload_to='slideshow/imagens')

class Meta:
	verbose_name = "Slideshow"
	verbose_name_plural = "Slideshow"

	def __str__(self):
		return self.titulo

class Quem_Somos(models.Model):
	titulo = models.CharField('Titulo', max_length = 100)   
	texto = models.CharField('Texto', max_length = 200)
	video_id = models.CharField(blank=False, max_length=32, default="")

	class Meta:
		verbose_name = "Quem Somos"
		verbose_name_plural = "Quem Somos"

	def __str__(self):
		return self.titulo

class Servicos(models.Model):
	titulo = models.CharField('Titulo', max_length = 100)   
	texto = models.CharField('Texto', max_length = 200)
	imagem = models.ImageField('Imagem', upload_to='slideshow/imagens')

	class Meta:
		verbose_name = "Serviço"
		verbose_name_plural = "Serviços"

	def __str__(self):
		return self.titulo