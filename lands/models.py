from django.db import models
from django.contrib.auth.models import User

class Land(models.Model):
    # Fields
    location = models.CharField(max_length=100)
    size = models.DecimalField(max_digits=10, decimal_places=2)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField()
    ownership_status = models.BooleanField(default=False, verbose_name="Ownership Status")
    confirmation_status = models.BooleanField(default=False, verbose_name="Confirmation Status")
    images = models.ImageField(upload_to="land_images", blank=True, null=True)
    document = models.FileField(upload_to="land_documents", blank=True, null=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name="lands", verbose_name="Owner")

    # Meta
    class Meta:
        verbose_name = "Land"
        verbose_name_plural = "Lands"

    # Methods
    def __str__(self):
        return f"{self.location} - {self.owner.username}"
