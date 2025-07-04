from functools import wraps
from django.http import HttpResponseForbidden

def group_permission_required(app_name, permission_type):
    def decorator(view_func):
        @wraps(view_func)
        def _wrapped_view(request, *args, **kwargs):
            user = request.user
            if not user.is_authenticated:
                return HttpResponseForbidden("No estás autenticado.")
            
            # Verificar permisos de los grupos del usuario
            for group in user.groups.all():
                if group.has_permission(app_name, permission_type):
                    return view_func(request, *args, **kwargs)
            
            return HttpResponseForbidden("No tienes los permisos necesarios.")
        return _wrapped_view
    return decorator