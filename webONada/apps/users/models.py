from django.db import models
from django.contrib.auth.models import AbstractUser 
# Create your models here.

class Group(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name
    
    def has_permission(self, app_name, permission_type):
        try:
            permission = self.permissions.get(app__name=app_name)
            return getattr(permission, f"can_{permission_type}", False)
        except GroupAppPermission.DoesNotExist:
            return False

class App(models.Model):
    name = models.CharField(max_length=100, unique=True)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.name
    
class GroupAppPermission(models.Model):
    group = models.ForeignKey(Group, on_delete=models.CASCADE, related_name="permissions")
    app = models.ForeignKey(App, on_delete=models.CASCADE, related_name="permissions")
    can_view = models.BooleanField(default=False)
    can_create = models.BooleanField(default=False)
    can_update = models.BooleanField(default=False)
    can_delete = models.BooleanField(default=False)

    class Meta:
        unique_together = ('group', 'app')  # Evitar duplicados de grupo-app

    def __str__(self):
        return f"{self.group.name} - {self.app.name}"
    
class User(AbstractUser):
    numero_documento = models.CharField(max_length=20, unique=True)
    imagen = models.ImageField(upload_to='users/', null=True, blank=True)
    numero_telefono = models.CharField(max_length=15, null=True, blank=True)
    direccion = models.CharField(max_length=100, null=True, blank=True)
    fecha_nacimiento = models.DateField(null=True, blank=True)
    primer_nombre = models.CharField(max_length=30, null=True, blank=True)
    segundo_nombre = models.CharField(max_length=30, null=True, blank=True)
    primer_apellido = models.CharField(max_length=30, null=True, blank=True)
    segundo_apellido = models.CharField(max_length=30, null=True, blank=True)

    groups = models.ManyToManyField(Group, related_name="users")

    class Meta:
        db_table = 'user'  # Cambia 'nombre_tabla_usuario' por el nombre deseado

    def __str__(self):
        return self.username
    
