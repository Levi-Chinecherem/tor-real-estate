from django.db import models
from django.contrib.auth.models import User

class Buyer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    full_name = models.CharField(max_length=255)
    house_address = models.CharField(max_length=255)
    state = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=15)

    class Meta:
        verbose_name = "Buyer"
        verbose_name_plural = "Buyers"

    def __str__(self):
        return self.full_name
