from rest_framework.permissions import BasePermission

class IsAuthorOrReadOnly(BasePermission):
    def has_object_permission(self, request, view, obj):
        # Permite las solicitudes GET, HEAD o OPTIONS para cualquier solicitud
        if request.method in ('GET', 'HEAD', 'OPTIONS'):
            return True
        # Permite solo si el autor del objeto es el mismo que el usuario solicitante
        return obj.author == request.user
