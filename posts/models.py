from django.contrib.auth.models import User
from django.db import models


class Post(models.Model):
    ESTADO_OPCIONES = [
        ('borrador', 'Borrador'),
        ('publicado', 'Publicado'),
        ('archivado', 'Archivado'),
    ]

    titulo = models.CharField(max_length=200)
    contenido = models.TextField()
    autor = models.ForeignKey(User, on_delete=models.CASCADE)
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    estado = models.CharField(max_length=20, choices=ESTADO_OPCIONES, default='borrador')

    def __str__(self):
        return self.titulo
