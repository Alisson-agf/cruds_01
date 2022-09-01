from django.shortcuts import render, redirect
from .models import Professor,Informatica, Motorista
from .forms import ProfessorForm, InformaticaForm, MotoristaForm

def professor_listar(request):
    professor = Professor.objects.all()
    contexto = {
        'professor_listar': professor
    }
    return render(request, '', contexto) 

def informatica_listar(request):
    informatica= Informatica.objects.all()
    contexto = {
        'listar_informatica': informatica
    }
    return render(request, '', contexto)

def motorista_listar(request):
    motorista= Motorista.objects.all()
    contexto = {
        'listar_motorista': motorista
    }
    return render(request, '', contexto) 


def professor_cadastro(request):
    form = ProfessorForm(request.POST or None)
    if form.is_valid():
            form.save()
            return redirect('')
    contexto = {
        'form': form
    }
    return render(request, '', contexto)

def informatica_cadastro(request):
    form = InformaticaForm(request.POST or None)
    if form.is_valid():
            form.save()
            return redirect('')
    contexto = {
        'form': form
    }
    return render(request, '', contexto)


def motorista_cadastro(request):
    form = MotoristaForm(request.POST or None)
    if form.is_valid():
            form.save()
            return redirect('')
    contexto = {
        'form': form
    }
    return render(request, '', contexto)

def professor_editar(request, id):
    professor =Professor.objects.get(pk=id)
    
    form = ProfessorForm(request.POST or None, instance=professor)
    if form.is_valid():
        form.save()
        return redirect('')
    
    contexto = {
        'form': form
    }

    return render(request, '', contexto) 


def informatica_editar(request, id):
    informatica=Informatica.objects.get(pk=id)
    
    form = InformaticaForm(request.POST or None, instance=informatica)
    if form.is_valid():
        form.save()
        return redirect('')
    
    contexto = {
        'form': form
    }

    return render(request, '', contexto)  

def motorista_editar(request, id):
    motorista =Motorista.objects.get(pk=id)
    
    form = MotoristaForm(request.POST or None, instance=motorista)
    if form.is_valid():
        form.save()
        return redirect('')
    
    contexto = {
        'form': form
    }

    return render(request, '', contexto) 



def professor_remover(request, id):
    professor = Professor.objects.get(pk=id)
    professor.delete()
    return redirect('')

def informatica_remover(request, id):
    infromatica= Informatica.objects.get(pk=id)
    infromatica.delete()
    return redirect('')

def motorista_remover(request, id):
    motorista= Motorista.objects.get(pk=id)
    motorista.delete()
    return redirect('')