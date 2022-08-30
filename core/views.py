from django.shortcuts import render, redirect
from .models import Emprego
from .forms import EmpregoForm

def emprego_listar(request):
    empregos = emprego.objects.all()
    contexto = {
        'emprego_cursos': emprego
    }
    return render(request, 'cursos.html', contexto)

def emprego_cadastro(request):
    form = CursosForm(request.POST or None)
    if form.is_valid():
            form.save()
            return redirect('emprego_listar')
    contexto = {
        'form': form
    }
    return render(request, 'curso_cadastro.html', contexto)


def emprego_editar(request, id):
    emprego = Emprego.objects.get(pk=id)
    
    form = EmpregoForm(request.POST or None, instance=emprego)
    if form.is_valid():
        form.save()
        return redirect('emprego_listar')
    
    contexto = {
        'form': form
    }

    return render(request, 'curso_cadastro.html', contexto)

def emprego_remover(request, id):
    emprego = Emprego.objects.get(pk=id)
    emprego.delete()
    return redirect('emprego_listar')