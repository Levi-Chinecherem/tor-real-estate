from django.contrib import admin
from .models import Seller

@admin.register(Seller)
class SellerAdmin(admin.ModelAdmin):
    list_display = ('user', 'full_name', 'state', 'phone_number', 'agreement_accepted')
    list_filter = ('state', 'agreement_accepted')
    search_fields = ('user__username', 'full_name', 'phone_number')
    readonly_fields = ('user',)  # Make user field read-only in admin

    def has_add_permission(self, request):
        # Disable the ability to add new sellers from the admin
        return False

    def has_delete_permission(self, request, obj=None):
        # Disable the ability to delete sellers from the admin
        return True
