# models.py in the Sellers app

from django.db import models
from django.contrib.auth.models import User

class Seller(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    full_name = models.CharField(max_length=255)
    house_address = models.CharField(max_length=255)
    state = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=15)
    profile_image = models.ImageField(upload_to="seller_profile_images", blank=True, null=True)
    agreement_accepted = models.BooleanField(default=False)

    def __str__(self):
        return self.user.username
