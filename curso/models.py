from django.db import models
from django.utils.text import slugify


class Curso(models.Model):
    nome = models.CharField(max_length=50, verbose_name='Nome')
    descricao = models.TextField(verbose_name='Descrição')
    thumbnail = models.ImageField(upload_to='thumb_curso', verbose_name='Thumbnail', blank=True, null=True)
    slug_curso = models.SlugField(verbose_name='Slug_curso', unique=True, blank=True, null=True)

    class Meta:
        verbose_name = 'Curso'
        verbose_name_plural = 'Cursos'

    def save(self, *args, **kwargs):
        if not self.slug_curso:
            slug_curso = f'{slugify(self.nome)}'
            self.slug_curso = slug_curso

        super().save(*args, **kwargs)

    def __str__(self) -> str:
        return self.nome


class Aula(models.Model):
    nome = models.CharField(max_length=50, verbose_name='Nome')
    descricao = models.TextField(verbose_name='Descrição', blank=True, null=True)
    aula = models.FileField(upload_to="aulas")
    curso = models.ForeignKey(Curso, on_delete=models.CASCADE, verbose_name='Curso')
    slug_aula = models.SlugField(verbose_name='Slug_aula', unique=True, blank=True, null=True)

    class Meta:
        verbose_name = 'Aula'
        verbose_name_plural = 'Aulas'

    def save(self, *args, **kwargs):
        if not self.slug_aula:
            slug_aula = f'{slugify(self.nome)}'
            self.slug_aula = slug_aula

        super().save(*args, **kwargs)

    def __str__(self) -> str:
        return self.nome



        