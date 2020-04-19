from django.db.models.signals import post_save
from django.dispatch import receiver

from user.models import MyUser, MyUserProfile


@receiver(post_save, sender=MyUser)
def product_created(sender, instance, created, **kwargs):
    if created:
        MyUserProfile.objects.create(user=instance)
