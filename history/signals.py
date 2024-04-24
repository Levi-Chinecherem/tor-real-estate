from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User
from sellers.models import Seller
from buyers.models import Buyer
from surveyors.models import Surveyor
from lands.models import Land
from .models import UserHistory, Role, LandHistory
# Signal receiver function to update user history


@receiver(post_save, sender=Seller)
@receiver(post_save, sender=Buyer)
@receiver(post_save, sender=Surveyor)
def update_user_history(sender, instance, created, **kwargs):
    user = instance.user
    user_history, created = UserHistory.objects.get_or_create(user=user)

    # Check if the user is a seller
    if hasattr(user, 'seller'):
        seller_role, _ = Role.objects.get_or_create(name='Seller')
        user_history.roles.add(seller_role)

    # Check if the user is a buyer
    if hasattr(user, 'buyer'):
        buyer_role, _ = Role.objects.get_or_create(name='Buyer')
        user_history.roles.add(buyer_role)

    # Check if the user is a surveyor
    if hasattr(user, 'surveyor'):
        surveyor_role, _ = Role.objects.get_or_create(name='Surveyor')
        user_history.roles.add(surveyor_role)

# Connect the signals
post_save.connect(update_user_history, sender=Seller)
post_save.connect(update_user_history, sender=Buyer)
post_save.connect(update_user_history, sender=Surveyor)


@receiver(post_save, sender=Land)
def create_land_history(sender, instance, created, **kwargs):
    if created:
        action = "Land uploaded"  # You can modify this action as needed
    else:
        action = "Land updated"  # Or provide different actions for create and update
    
    # Create LandHistory instance
    LandHistory.objects.create(land=instance, action=action, user=instance.owner)
