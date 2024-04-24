from django.contrib import admin
from .models import Land

@admin.register(Land)
class LandAdmin(admin.ModelAdmin):
    list_display = ('location', 'size', 'price', 'ownership_status', 'confirmation_status', 'owner')
    list_filter = ('ownership_status', 'confirmation_status')
    search_fields = ('location', 'owner__username')
    readonly_fields = ('owner',)

    fieldsets = (
        (None, {
            'fields': ('location', 'size', 'price', 'description', 'images', 'document', 'owner')
        }),
        ('Status', {
            'fields': ('ownership_status', 'confirmation_status'),
            'classes': ('collapse',)  # Hide by default
        }),
    )

    def has_delete_permission(self, request, obj=None):
        return False

    def get_readonly_fields(self, request, obj=None):
        # Prevent editing of fields other than 'location', 'size', 'price', 'description'
        if obj:
            return ['owner']
        else:
            return []

    def get_queryset(self, request):
        queryset = super().get_queryset(request)
        # Prefetch related owner data to avoid extra queries
        return queryset.select_related('owner')
