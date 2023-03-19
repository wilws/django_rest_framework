from rest_framework import permissions

class IsStaffEditorPermission(permissions.DjangoModelPermissions):

    perms_map = {
        'GET': ['%(app_label)s.view_%(model_name)s'],   # GET request need to have permission
        'OPTIONS': [],
        'HEAD': [],
        'POST': ['%(app_label)s.add_%(model_name)s'],
        'PUT': ['%(app_label)s.change_%(model_name)s'],
        'PATCH': ['%(app_label)s.change_%(model_name)s'],
        'DELETE': ['%(app_label)s.delete_%(model_name)s'],
    }