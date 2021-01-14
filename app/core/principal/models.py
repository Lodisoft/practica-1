from django.db import models

# Create your models here.
class Person(models.Model):
    id = models.AutoField(primary_key = True)
    name = models.CharField(max_length=100)
    lastname = models.CharField(max_length=120)
    email = models.EmailField(max_length=200)

    def __str__(self):
        return self.name
    

    class Meta:
        verbose_name = "Persona"
        verbose_name_plural = "Personas"
        ordering = ['id']