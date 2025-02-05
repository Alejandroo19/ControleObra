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
        forma_pagamento = request.POST.get('forma_pagamento')
        if valor and forma_pagamento:
            ValorAdicionado.objects.create(
                obra=obra,
                valor=valor,
                descricao=descricao,
                forma_pagamento=forma_pagamento
            )
            obra.verificar_status()  # Verifica e atualiza o status da obra
            if obra.status == 'finalizada':
                return redirect(f'{request.path}?finalizada=true')
            return redirect('detalhe_obra', obra_id=obra.id)
    # Verifica se a query string "finalizada=true" está presente
    finalizada = request.GET.get('finalizada') == 'true'

    return render(request, 'obra/detalhe_obra.html', {'obra': obra, 'valores': valores, 'finalizada': finalizada})