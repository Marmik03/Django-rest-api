from rest_framework import permissions

class UpdateOwnProfile(permissions.BasePermission):
    """Ällow User to Edit there own Profile"""


    def has_object_permission(self, request, view, obj):
        """Check User is trying to edit there own Profile"""
        if request.method in permissions.SAFE_METHODS :
            return True


        return obj.id == request.user.id


class UpdateOwnStatus(permissions.BasePermission):
    """Allow user to update their own status"""

    def has_object_permission(self, request, view, obj):
        """Check User is trying to update there own status"""
        if request.method in permissions.SAFE_METHODS :
            return True

        return obj.user_profile.id == request.user.id
