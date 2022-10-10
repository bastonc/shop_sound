from rest_framework.permissions import BasePermission


class IsContentManager(BasePermission):
    def has_permission(self, request, view):
        if request.user.is_authenticated and request.user.is_content:
            return True
        return False
