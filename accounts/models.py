from django.db import models


class Student(models.Model):
    """Un estudiante: solo datos de contacto, sin credenciales."""
    nombre = models.CharField(max_length=150, unique=False)
    contra = models.CharField(max_length=128, unique=False)
    creado = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.nombre} <{self.contra}>'
