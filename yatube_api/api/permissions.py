from rest_framework import permissions

CANNOT_UPDATE_OTHER_CONTENT = 'Изменение чужого контента запрещено!'


class IsAuthorOrReadOnly(permissions.BasePermission):
    """Разрешение для редактирования только автором или чтения для всех"""
    message = CANNOT_UPDATE_OTHER_CONTENT

    def has_permission(self, request, view):
        return (
            request.method in permissions.SAFE_METHODS
            or request.user.is_authenticated
        )

    def has_object_permission(self, request, view, obj):
        return (
            request.method in permissions.SAFE_METHODS
            or obj.author == request.user)
