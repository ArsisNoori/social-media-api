# social/permissions.py
from rest_framework import permissions


class IsAuthorOrReadOnly(permissions.BasePermission):
    """
    فقط نویسنده اجازه‌ی ویرایش و حذف داره.
    دیگران فقط می‌تونن بخونن (GET, HEAD, OPTIONS).
    """

    def has_object_permission(self, request, view, obj):
        # متدهای ایمن (خواندنی) برای همه مجاز است
        if request.method in permissions.SAFE_METHODS:
            return True

        # ویرایش و حذف فقط برای نویسنده
        return obj.author == request.user