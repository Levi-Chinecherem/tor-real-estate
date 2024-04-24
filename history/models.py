from django.db import models
from django.contrib.auth.models import User
from sellers.models import Seller
from buyers.models import Buyer
from surveyors.models import Surveyor
from lands.models import Land

class UserHistory(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    roles = models.ManyToManyField('Role', related_name='users', blank=True)

    def __str__(self):
        return f"{self.user.username}'s History"

    def get_roles(self):
        return ', '.join([role.name for role in self.roles.all()])
    
    def save(self, *args, **kwargs):
        # Clear existing roles
        # Not necessary because we're handling this in the update_user_history signal receiver
        # self.roles.clear()

        super().save(*args, **kwargs)

class Role(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class LandHistory(models.Model):
    land = models.ForeignKey(Land, on_delete=models.CASCADE, related_name='histories')
    action = models.CharField(max_length=255)  # E.g., "Land uploaded", "Land approved by surveyor", "Bid placed by buyer"
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.action} for Land: {self.land.location}"
