from django.contrib import admin
from .models import Group, App, GroupAppPermission, User

# Registrar Permisos
@admin.register(Group)
class GroupAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    list_filter = ('name',)

@admin.register(App)
class AppAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'description')
    list_filter = ('name',)


@admin.register(GroupAppPermission)
class GroupAppPermissionAdmin(admin.ModelAdmin):
    list_display = ('group', 'app', 'can_view', 'can_create', 'can_update', 'can_delete')
    list_filter = ('group', 'app')

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('id', 'primer_nombre', 'segundo_nombre', 'primer_apellido', 'segundo_apellido', 'numero_documento', 'email', 'get_groups')
    list_filter = ('numero_documento', 'email')

    def get_groups(self, obj):
        return ", ".join([group.name for group in obj.groups.all()])
    get_groups.short_description = 'Groups'