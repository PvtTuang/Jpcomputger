from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User
from .models import Profile, Role

@receiver(post_save, sender=User)
def create_or_update_user_profile(sender, instance, created, **kwargs):
    if created:
        role, _ = Role.objects.get_or_create(name='Customer') 
        profile, _ = Profile.objects.get_or_create(user=instance, defaults={'role': role})
        instance.profile = profile  
        instance.save()  