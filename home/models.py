from django.db import models
from django.contrib.auth.models import User   

# Create your models here.

class Project(models.Model):
    title=models.CharField(max_length=100, verbose_name='Titulo')
    description=models.TextField(verbose_name='Descripcion')
    author = models.ForeignKey(User, verbose_name="Editor", on_delete=models.CASCADE, null=True)
    created=models.DateTimeField(auto_now_add=True, verbose_name='fecha creacion')
    updated=models.DateTimeField(auto_now=True, verbose_name='fecha actualizacion')

    class Meta:
        verbose_name='Proyecto'
        verbose_name_plural='proyectos'
        ordering=['-created']

    def __str__(self):
        return self.title

    
