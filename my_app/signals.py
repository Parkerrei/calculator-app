from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver 
from django.contrib.auth.models import User
from .models import Profile


# Using Decorator For Receiving Signals  #
@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)


@receiver(post_delete, sender=User)
def profile_delete(sender, instance, **kwargs):
    if instance:
        profile = getattr(User, 'username', None)        
        if profile:
                print (f'{instance.username} has been  deleted!')
                
             

