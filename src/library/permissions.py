from rest_framework.permissions import BasePermission


class IsApproved(BasePermission):
    message = "Batch not ready yet"

    def has_permission(self, request, view):
        return request.user.has_perm('accounts.access_workshops')
