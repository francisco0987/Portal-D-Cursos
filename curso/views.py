from django.http import HttpResponse
from django.shortcuts import redirect, render

from .models import Aula, Curso


def home(request):
    cursos = Curso.objects.all()
    usuario_logado = request.session.get('usuario')
    return render(request, 'home.html', {'cursos': cursos, 'usuario_logado': usuario_logado})

def curso(request, slug_curso):
    usuario_logado = request.session.get('usuario')

    if usuario_logado:
        curso = Curso.objects.get(slug_curso=slug_curso)
        aulas = Aula.objects.filter(curso=curso)
        
        print(aulas[0].aula.url)
        

        return render(request, 'curso.html', {'curso': curso, 'aulas': aulas, 'usuario_logado': usuario_logado})
    else:
        return redirect('/auth/login')
    


def aula(request, slug_aula):
    usuario_logado = request.session.get('usuario')

    if usuario_logado:
        aula = Aula.objects.get(slug_aula=slug_aula)

        return render(request, 'aula.html', {'aula': aula, 'usuario_logado': usuario_logado})
    else:
        return redirect('/auth/login/')
