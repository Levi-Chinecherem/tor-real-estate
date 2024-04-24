from django.contrib import admin
from .models import UserHistory, Role, LandHistory

class RoleAdmin(admin.ModelAdmin):
    list_display = ['name']

class UserHistoryAdmin(admin.ModelAdmin):
    list_display = ['user', 'get_roles']
    filter_horizontal = ['roles']

    def get_roles(self, obj):
        return ", ".join([role.name for role in obj.roles.all()])
    get_roles.short_description = 'Roles'

class LandHistoryAdmin(admin.ModelAdmin):
    list_display = ['land', 'action', 'user', 'timestamp']

admin.site.register(Role, RoleAdmin)
admin.site.register(UserHistory, UserHistoryAdmin)
admin.site.register(LandHistory, LandHistoryAdmin)
