from datetime import datetime

from django.db import models
from django.contrib.auth.models import AbstractUser, UserManager





class Category(models.Model):
    name = models.CharField(max_length=100)
    created_at = models.DateTimeField(default=datetime.now)
    status = models.CharField(max_length=50,default="Active")

    def __str__(self):
        return self.name
    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'


class MyUser(AbstractUser):
    mobile = models.CharField(max_length=20, blank=True)
    location = models.CharField(max_length=50, blank=True)
    birth_date = models.DateField(null=True, blank=True)
    photo = models.ImageField(
        default='https://f0.pngfuel.com/png/184/113/portrait-icon-user-profile-computer-icons-profile-png-clip-art.png',
        upload_to='user_photos/', blank=True, null=True)
    favourite_category = models.ForeignKey(Category, on_delete=models.CASCADE,related_name="subscribers",blank=True,null=True)





class Product(models.Model):

    name = models.CharField(max_length=200)
    created_at = models.DateTimeField(default=datetime.now)
    status = models.CharField(max_length=50,default="Available")
    category = models.ForeignKey(Category, on_delete=models.CASCADE,related_name="products")
    photo=models.ImageField(default='https://webstore.iea.org/content/images/thumbs/default-image_450.png',
                            upload_to='user_photos/',blank=True, null=True)
    price=models.IntegerField(default=1000)
    def __str__(self):
        return 'name :{}, category: {}'.format(self.name,self.category)


class OrderManager(models.Manager):
    def for_user(self,user):
        return self.filter(created_by=user)

class Order(models.Model):
    objects=OrderManager()
    status = models.CharField(max_length=50, default="in process")
    product=models.ForeignKey(Product,on_delete=models.CASCADE,related_name="orders")
    created_by=models.ForeignKey(MyUser,on_delete=models.CASCADE,related_name="orders")
    created_at = models.DateTimeField(default=datetime.now, blank=True)
    address=models.CharField(max_length=100,blank=True,default="No Address")
    quantity=models.IntegerField(default=1)


class Notification(models.Model):
    user=models.ForeignKey(MyUser,on_delete=models.CASCADE,related_name="notifications")
    product=models.ForeignKey(Product,on_delete=models.CASCADE,related_name="subscribers")