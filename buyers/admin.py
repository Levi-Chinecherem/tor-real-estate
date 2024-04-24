from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import Buyer

@admin.register(Buyer)
class BuyerAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'house_address', 'state', 'phone_number', 'user')
    search_fields = ('full_name', 'house_address', 'state', 'phone_number', 'user__username')
    list_filter = ('state',)
    ordering = ('full_name',)
    readonly_fields = ('user',)

    fieldsets = (
        (None, {
            'fields': ('full_name', 'house_address', 'state', 'phone_number', 'user')
        }),
    )

    def has_delete_permission(self, request, obj=None):
        return False

    def get_readonly_fields(self, request, obj=None):
        # Prevent editing of fields other than 'full_name', 'house_address', 'state', 'phone_number'
        if obj:
            return ['user']
        else:
            return []

    def get_queryset(self, request):
        queryset = super().get_queryset(request)
        # Prefetch related user data to avoid extra queries
        return queryset.select_related('user')
