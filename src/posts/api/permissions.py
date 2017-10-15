from rest_framework.permissions import BasePermission, SAFE_METHODS


class IsOwnerOrReadOnly(BasePermission):
    message = "You should be Owner of this post"

    def has_permission(self, request, view):
        my_safe_method = ['PUT', 'GET']
        if request.method in my_safe_method:
            return True
        return False

    def has_object_permission(self, request, view, obj):
        if request.method in SAFE_METHODS:
            return True
        return obj.user == request.user
