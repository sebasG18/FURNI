from django.db import models

# Create your models here.

class Content(models.Model):
    title=models.CharField(max_length=100, verbose_name='Titulo')
    description=models.TextField(verbose_name='Descripcion')
    image1=models.ImageField(verbose_name='Imagen1', upload_to='projects')
    Seconddes1=models.TextField(verbose_name='Descripcion')
    image2=models.ImageField(verbose_name='Imagen2', upload_to='projects')
    Seconddes2=models.TextField(verbose_name='Descripcion')
    image3=models.ImageField(verbose_name='Imagen3', upload_to='projects')
    Seconddes3=models.TextField(verbose_name='Descripcion')
    image4=models.ImageField(verbose_name='Imagen4', upload_to='projects')
    Seconddes4=models.TextField(verbose_name='Descripcion')
    created=models.DateTimeField(auto_now_add=True, verbose_name='fecha creacion')
    updated=models.DateTimeField(auto_now=True, verbose_name='fecha actualizacion')

    class Meta:
        verbose_name='Contenido'
        verbose_name_plural='Contenidos'
        ordering=['-created']

    def __str__(self):
        return self.title
