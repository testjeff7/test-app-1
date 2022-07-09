from django.db import models

# Create your models here.
class Inicio(models.Model):
    image = models.ImageField(verbose_name='Image do Inicio', upload_to='fotos')
    titulo = models.CharField(verbose_name='Titulo do Inicio' ,max_length=250)
    descricao = models.TextField(verbose_name='Descrição')
    text_button = models.CharField(verbose_name='Texto do Botão', max_length=20)

    def __str__(self):
        return f'{self.titulo}'

class Produto(models.Model):
    image = models.ImageField(verbose_name='Image do produto', upload_to='produto')
    titulo = models.CharField(max_length=250)
    descricao = models.TextField()

    def __str__(self):
        return f'{self.titulo}'

class Mensagem(models.Model):
    image = models.ImageField(upload_to='mensagem')
    titulo = models.CharField(max_length=250)
    descricao = models.TextField()
    link = models.CharField(max_length=100)
    mensagem_link = models.CharField(max_length=100)

    def __str__(self):
        return f'{self.titulo}'

class Depoimento(models.Model):
    depoimento = models.CharField(max_length=300)
    image = models.ImageField(upload_to='depoimento')
    autor = models.CharField(max_length=50)
    empresa = models.CharField(max_length=50)

    def __str__(self):
        return f'{self.autor}'

class Contato(models.Model):
    endereco = models.CharField(max_length=250)
    email = models.EmailField()
    telefone = models.CharField(max_length=12)
    twitter = models.CharField(max_length=100)
    facebook = models.CharField(max_length=100)
    instagram = models.CharField(max_length=100)

    def __str__(self):
        return f'{self.email}'

        
class FormContato(models.Model):
    nome = models.CharField(max_length=150)
    telefone = models.CharField(max_length=12)
    email = models.EmailField()