from django.contrib import admin
from django.contrib.admin import BooleanFieldListFilter
from .models import Surveyor, PotentialSellerField

# Custom Field to determine if user is a potential seller
class PotentialSellerFieldAdmin(admin.ModelAdmin):
    def pre_save(self, model_instance, add):
        # Check if the user is a seller
        is_seller = model_instance.user.seller.exists()
        # Set the field value based on whether the user is a seller
        return is_seller

# Register Surveyor model with custom admin display
class SurveyorAdmin(admin.ModelAdmin):
    list_display = ('user', 'approved', 'is_potential_seller_admin')
    list_filter = ('approved', 'is_potential_seller')
    readonly_fields = ('is_potential_seller_admin',)

    def is_potential_seller_admin(self, obj):
        # Display the value of is_potential_seller
        return obj.is_potential_seller
    is_potential_seller_admin.boolean = True
    is_potential_seller_admin.short_description = 'Potential Seller'

# Register the models with the custom admin
admin.site.register(Surveyor, SurveyorAdmin)
