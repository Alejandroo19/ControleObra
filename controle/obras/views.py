from django.shortcuts import render, redirect, get_object_or_404
from .models import Obra, ValorAdicionado


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
    obra = get_object_or_404(Obra, id=obra_id)
    valores = obra.valores_adicionados.all()

    if request.method == 'POST':
        valor = request.POST.get('valor')
        descricao = request.POST.get('descricao')
        if valor:
            ValorAdicionado.objects.create(obra=obra, valor=valor, descricao=descricao)
            obra.verificar_status()  # Verifica e atualiza o status da obra
            if obra.status == 'finalizada':
                # Redireciona para a página com um indicador de sucesso
                return redirect(f'{request.path}?finalizada=true')

    # Verifica se a query string "finalizada=true" está presente
    finalizada = request.GET.get('finalizada') == 'true'

    return render(request, 'obra/detalhe_obra.html', {'obra': obra, 'valores': valores, 'finalizada': finalizada})