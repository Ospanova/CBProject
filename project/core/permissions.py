from rest_framework import permissions


class HasPermission(permissions.BasePermission):
    """
        Permission class for detecting the permission of actions for user
    """

    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True

        return request.user and (obj.reviewer == request.user
                                 or request.user.is_superuser)
