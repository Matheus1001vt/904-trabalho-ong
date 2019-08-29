from django.shortcuts import render
from website.models import Pessoa, Ong

# Create your views here.

def index(request):

    if request.method == 'POST':
        pessoa = Pessoa()
        pessoa.nome = request.POST.get('nome')
        pessoa.sobrenome = request.POST.get('sobrenome')
        pessoa.data_nascimento = request.POST.get('data_nascimento')
        pessoa.email = request.POST.get('email')
        pessoa.str_cep = request.POST.get('str_cep')
        pessoa.str_numero = request.POST.get('str_numero')
        pessoa.complemento = request.POST.get('complemento')
        pessoa.genero = request.POST.get('genero')
        pessoa.telefone = request.POST.get('telefone')
        pessoa.celular = request.POST.get('celular')
        pessoa.motivo = request.POST.get('motivo')
        pessoa.save()

        contexto = {
            'nome': pessoa.nome
        }
        return render(request, 'index.html', contexto)

 
    return render(request, 'index.html')


def pessoas(request):
    pessoas = Pessoa.objects.filter(ativo=True).all()
    
    contexto = {
        'pessoas': pessoas
    }
    return render(request, 'pessoas.html', contexto)



    if request.method == 'POST':
        ong = Ong()
        ong.nome_responsavel = request.POST.get('nome')
        ong.nome_ong = request.POST.get('sobrenome')
        ong.str_cep = request.POST.get('str_cep')
        ong.str_numero = request.POST.get('str_numero')
        ong.complemento = request.POST.get('complemento')
        ong.telefone = request.POST.get('telefone')
        ong.whatsapp = request.POST.get('whatsapp')
        ong.horario_funcionamnto = request.POST.get('horario')
        ong.observacao = request.POST.get('observacao')
        ong.save()

        contexto = {
            'ong': ong.nome_responsavel
        }
        return render(request, 'index.html', contexto)

 
    return render(request, 'index.html')