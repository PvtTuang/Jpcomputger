from django.core.exceptions import PermissionDenied

def block_role_required(view_func):
    def _wrapped_view_func(request, *args, **kwargs):
        if request.user.profile.role.name == 'Blocked':
            raise PermissionDenied
        return view_func(request, *args, **kwargs)
    return _wrapped_view_func