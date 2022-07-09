from django.shortcuts import render

from .models import Contato, Depoimento, Inicio, Mensagem, Produto, FormContato

# Create your views here.
def home(request):

    inicio = Inicio.objects.last()

    produtos = Produto.objects.all()
    mensagem = Mensagem.objects.last()
    depoimento = Depoimento.objects.all()
    contato = Contato.objects.last()
    
    context = {
        'inicio': inicio,
        'produtos': produtos,
        'mensagem': mensagem,
        'depoimentos': depoimento,
        'contato': contato
    }

    if request.method == 'POST':
        nome_form = request.POST['nome']
        telefone = request.POST['telefone']
        email = request.POST['email']

        form = FormContato(nome=nome_form, telefone=telefone, email=email)
        form.save()

    return render(request, 'index.html', context)


