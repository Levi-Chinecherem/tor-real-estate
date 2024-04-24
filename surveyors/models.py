from django.db import models
from django.contrib.auth.models import User
from django.core.exceptions import ObjectDoesNotExist

class PotentialSellerField(models.BooleanField):
    def pre_save(self, model_instance, add):
        # Check if the user is a seller
        try:
            is_seller = model_instance.user.seller is not None
            is_seller = True
        except ObjectDoesNotExist:
            is_seller = False
        # Return a boolean value
        return is_seller

class Surveyor(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    approved = models.BooleanField(default=False)
    full_name = models.CharField(max_length=255)
    house_address = models.CharField(max_length=255)
    state = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=15)
    image = models.ImageField(upload_to="surveyor_images", blank=True, null=True)
    resume = models.FileField(upload_to="surveyor_resumes", blank=True, null=True)
    is_potential_seller = PotentialSellerField(default=False, editable=False)

    def __str__(self):
        return self.user.username
