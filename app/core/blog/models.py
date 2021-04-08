from django.db import models
from django.contrib.auth.models import User
from django.utils.text import slugify
from ckeditor.fields import RichTextField

# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.PROTECT)
    website = models.URLField(max_length=200, blank=True)
    facebook = models.URLField(max_length=200, blank=True)
    instagram = models.URLField(max_length=200, blank=True)
    twitter = models.URLField(max_length=200, blank=True)
    description = models.TextField(verbose_name="Descripcion", blank="True")
    photo = models.ImageField(upload_to='users/pictures',blank=True,null=True)
    created_on = models.DateTimeField(auto_now_add=True, verbose_name="Fecha Creación")
    updated_on = models.DateTimeField(auto_now=True, verbose_name="Fecha Edición")

    class Meta:
        verbose_name='Perfil'
        verbose_name_plural = 'Perfiles'
        ordering = ['id']

    def __str__(self):
        """Return username."""
        return self.user.username

class Tag(models.Model):
    name = models.CharField(max_length=100, verbose_name="Nombre",unique=True)
    created_on = models.DateTimeField(auto_now_add=True, verbose_name="Fecha Creación")
    updated_on = models.DateTimeField(auto_now=True, verbose_name="Fecha Edición")

    class Meta:
        verbose_name='Etiqueta'
        verbose_name_plural = 'Etiquetas'
        ordering = ['id']

    def __str__(self):
        return self.name

class Category(models.Model):
    name = models.CharField(max_length=100,unique=True)
    created_on = models.DateTimeField(auto_now_add=True, verbose_name="Fecha Creación")
    updated_on = models.DateTimeField(auto_now=True, verbose_name="Fecha Edición")

    class Meta:
        verbose_name='Categoría'
        verbose_name_plural = 'Categorias'
        ordering = ['id']

    def __str__(self):
        return self.name

class Post(models.Model):
    title = models.CharField(max_length=100, verbose_name="Titulo")
    url = models.SlugField(max_length=255, unique=True)
    image_header = models.ImageField(upload_to='posts/photos', verbose_name="Imagen del Post")
    teaser = models.CharField(max_length=255, verbose_name="Introducción")
    body = RichTextField()
    is_draft = models.BooleanField(default=True)
    views = models.PositiveIntegerField(default=0)
    tags = models.ManyToManyField(Tag)
    category = models.ForeignKey(Category, verbose_name="Categoría", on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.PROTECT)
    profile = models.ForeignKey(Profile, on_delete=models.PROTECT)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name='Publicación'
        verbose_name_plural = 'Publicaciones'
        ordering = ['id']


    def __str__(self):
        """Return title and username."""
        return '{} by @{}'.format(self.title, self.user.username)
    

    def save(self, *args, **kwargs):
        self.url = slugify(self.title)
        super(Post, self).save(*args, **kwargs)

class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.PROTECT)
    profile = models.ForeignKey(Profile, on_delete=models.PROTECT)
    post = models.ForeignKey(Post, on_delete=models.PROTECT)
    comment = models.CharField(max_length=5000)

    class Meta:
        verbose_name='Comentario'
        verbose_name_plural = 'Comentarios'
        ordering = ['id']

    def __str__(self):
        return self.comment
    