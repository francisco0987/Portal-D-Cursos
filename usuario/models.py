from django.db import models


class Usuario(models.Model):
    nome = models.CharField(max_length=50, verbose_name='Nome')
    email = models.EmailField(verbose_name='Email', unique=True)
    senha = models.CharField(max_length=64)

    class Meta:
        verbose_name = 'Usuário'
        verbose_name_plural = 'Usuários'

    def __str__(self) -> str:
        return self.nome
