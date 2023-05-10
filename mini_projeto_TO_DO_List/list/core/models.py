from django.db import models

class cadastro_tarefas(models.Model):
    titulo = models.CharField('titulo', max_length=100)
    data = models.DateField('data')
    descricao = models.CharField('descricao', max_length=200)

    def __str__(self) -> str:
        return self.titulo