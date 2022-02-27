from rest_framework.permissions import BasePermission, SAFE_METHODS


class ProfileUpdatePermission(BasePermission):
    """Allow user to only update their own profile."""

    def has_object_permission(self, request, view, obj) -> bool:
        """Check if user is trying to update their own profile."""
        if request.method in SAFE_METHODS:
            return True

        return obj.id == request.user.id