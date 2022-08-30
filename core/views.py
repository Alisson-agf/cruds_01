from django.shortcuts import render, redirect
from .models import emprego
from .forms import EmpregoForm

def emprego_listar(request):
    empregos = emprego.objects.all()
    contexto = {
        'lista_cursos': emprego
    }
    return render(request, 'cursos.html', contexto)

def curso_cadastro(request):
    form = CursosForm(request.POST or None)
    if form.is_valid():
            form.save()
            return redirect('emprego_listar')
    contexto = {
        'form': form
    }
    return render(request, 'curso_cadastro.html', contexto)


def curso_editar(request, id):
    curso = Curso.objects.get(pk=id)
    
    form = CursosForm(request.POST or None, instance=curso)
    if form.is_valid():
        form.save()
        return redirect('cursos_listar')
    
    contexto = {
        'form': form
    }

    return render(request, 'curso_cadastro.html', contexto)

def curso_remover(request, id):
    curso = Curso.objects.get(pk=id)
    curso.delete()
    return redirect('cursos_listar')