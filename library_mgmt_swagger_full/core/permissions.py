from rest_framework.permissions import BasePermission, SAFE_METHODS
from django.conf import settings

def in_group(user, name):
    return user.is_authenticated and user.groups.filter(name=name).exists()

class IsLibrarianOrReadOnly(BasePermission):
    def has_permission(self, request, view):
        if request.method in SAFE_METHODS:
            return True
        return (request.user and request.user.is_staff) or in_group(request.user, settings.LIBRARIAN_GROUP)

class IsMember(BasePermission):
    def has_permission(self, request, view):
        return request.user and (in_group(request.user, settings.MEMBER_GROUP) or request.user.is_staff)
