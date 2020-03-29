from rest_framework import permissions

class UpdateOwnProfile(permissions.BasePermission):
    """Ällow User to Edit there own Profile"""


    def has_object_permission(self, request, view, obj):
        """Check User is trying to edit there own Profile"""
        if request.method in permissions.SAFE_METHODS :
            return True


        return obj.id == request.user.id
