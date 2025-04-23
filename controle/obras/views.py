from django.shortcuts import render, redirect, get_object_or_404
from .models import Obra, ValorAdicionado, FuncionarioObra 


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
    funcionarios = obra.funcionarios.all()

    if request.method == 'POST':
        if 'valor' in request.POST:
            # Lógica para valor
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
                obra.verificar_status()
                if obra.status == 'finalizada':
                    return redirect(f'{request.path}?finalizada=true')
                return redirect('detalhe_obra', obra_id=obra.id)

        elif 'nome_funcionario' in request.POST:
            nome = request.POST.get('nome_funcionario')
            diaria = request.POST.get('valor_diaria')

            if nome and diaria:
                FuncionarioObra.objects.create(
                    obra=obra,
                    nome=nome,
                    valor_diaria=diaria
                )
                return redirect('detalhe_obra', obra_id=obra.id)

    finalizada = request.GET.get('finalizada') == 'true'
    return render(request, 'obra/detalhe_obra.html', {
        'obra': obra,
        'valores': valores,
        'funcionarios': funcionarios,
        'finalizada': finalizada
    })