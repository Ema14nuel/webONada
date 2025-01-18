from django.db import models
from django.contrib.auth.models import AbstractUser 
# Create your models here.

class User(AbstractUser):
    numero_documento = models.CharField(max_length=20, unique=True)
    imagen = models.ImageField(upload_to='usuarios/', null=True, blank=True)
    numero_telefono = models.CharField(max_length=15, null=True, blank=True)
    direccion = models.CharField(max_length=100, null=True, blank=True)
    fecha_nacimiento = models.DateField(null=True, blank=True)
    primer_nombre = models.CharField(max_length=30, null=True, blank=True)
    segundo_nombre = models.CharField(max_length=30, null=True, blank=True)
    primer_apellido = models.CharField(max_length=30, null=True, blank=True)
    segundo_apellido = models.CharField(max_length=30, null=True, blank=True)

    groups = models.ManyToManyField('auth.Group', related_name='custom_user_groups', blank=True)
    user_permissions = models.ManyToManyField('auth.Permission', related_name='custom_user_permissions', blank=True)

    class Meta:
        db_table = 'user'  # Cambia 'nombre_tabla_usuario' por el nombre deseado

    def __str__(self):
        return self.username
    
