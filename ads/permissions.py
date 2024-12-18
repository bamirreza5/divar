from rest_framework import permissions

class IsOwner(permissions.BasePermission):
    def has_object_permissions(self, request, view, obj):
        # اجازه فقط اگر کاربر جاری مالک آگهی باشد
        return obj.user == request.user
