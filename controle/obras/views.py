from django.shortcuts import render, redirect, get_object_or_404
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


def detalhe_obra(request, obra_id):
    obra = get_object_or_404(Obra, id=obra_id)  # Busca a obra ou retorna 404 se não existir
    return render(request, 'obra/detalhe_obra.html', {'obra': obra})