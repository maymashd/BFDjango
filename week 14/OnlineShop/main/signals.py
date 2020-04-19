from django.db.models.signals import post_save
from django.dispatch import receiver

from main.models import MyUser, Product, Category, Notification


@receiver(post_save, sender=Product)
def product_created(sender, instance, created, **kwargs):
    if created:
        category=instance.category
        users=category.subscribers.all()
        for user in users:
            Notification.objects.create(user=user,product=instance)

