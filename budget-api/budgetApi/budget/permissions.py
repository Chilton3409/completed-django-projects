from rest_framework import permissions

class IsUserOrReadOnly(permissions.BasePermission):
    #custom only allow users to edit budget 
    def has_object_permission(self, request, view, obj):
        #read permissions are allowed to any request
        #always allow get, head, or options requests
        if request.method in permissions.SAFE_METHODS:
            return True 

        #write permissions are only only to the actual owner
        return obj.user == request.user
        
        