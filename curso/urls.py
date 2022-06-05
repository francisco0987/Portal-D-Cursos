from django.urls import path

from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('curso/<slug:slug_curso>', views.curso, name='curso'),
    path('aula/<slug:slug_aula>', views.aula, name='aula'),
]
