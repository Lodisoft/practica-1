from django.db import models
from django.core.validators import MinLengthValidator


# Create your models here.
class Area(models.Model):
    name = models.CharField(max_length=50, verbose_name = 'Nombre', validators=[MinLengthValidator(4)])
    description = models.TextField(verbose_name = 'Descipción', validators=[MinLengthValidator(5)])

    class Meta:
        verbose_name = "Área"
        verbose_name_plural = "Areas"
        ordering = ['id']
    
    def __str__(self):
        return self.name


class Category(models.Model):
    name = models.CharField(max_length=50, validators=[MinLengthValidator(4)])
    desciption = models.TextField(verbose_name = 'Descripción', validators=[MinLengthValidator(4)])
    

    class Meta:
        verbose_name = "Categoría"
        verbose_name_plural = "Categorías"
        ordering = ['id']

    def __str__(self):
        return self.name

class Product(models.Model):
    code = models.CharField(max_length=200, verbose_name = 'Codigo', unique = True, blank=False, validators=[MinLengthValidator(10)])
    name = models.CharField(max_length=150, verbose_name = 'Nombre', blank=False, validators=[MinLengthValidator(4)])
    description = models.TextField(verbose_name = 'Descripción', validators=[MinLengthValidator(10)])
    stock = models.PositiveIntegerField(verbose_name = 'Stock', blank= False, default = 1)
    min_stock = models.PositiveIntegerField(verbose_name = 'Stock Minimo', blank= True, default = 1)
    area = models.ForeignKey(Area, on_delete=models.CASCADE, verbose_name = 'Área')
    categories = models.ManyToManyField('Category', verbose_name = 'Categorias')

    class Meta:
        verbose_name = "Producto"
        verbose_name_plural = "Productos"
        ordering = ['id']

    def __str__(self):
        return self.name
