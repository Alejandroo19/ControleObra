from django.shortcuts import render, redirect
from .models import Obra

def listar_obras(request):
    obras = Obra.objects.all()
    return render(request, 'obra/listar_obras.html', {'obras': obras})

def criar_obra(request):
    if request.method == 'POST':
        nome = request.POST.get('nome')
        valor = request.POST.get('valor')
        Obra.objects.create(nome=nome, valor=valor)
        return redirect('listar_obras')
    return render(request, 'criar_obra.html')