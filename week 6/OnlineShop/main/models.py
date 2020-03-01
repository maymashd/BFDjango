from datetime import datetime

from django.db import models
from django.contrib.auth.models import AbstractUser, UserManager



class MyUser(AbstractUser):
    mobile=models.CharField(max_length=20,blank=True)
    location=models.CharField(max_length=50,blank=True)
    birth_date=models.DateField(null=True,blank=True)

    def to_json(self):
        return {
            'id ': self.id,
            'username ': self.username,
            'email ': self.email,
        }


class Category(models.Model):
    name = models.CharField(max_length=100)
    created_at = models.DateTimeField(default=datetime.now)
    status = models.CharField(max_length=50,default="Active")

    def __str__(self):
        return self.name
    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'



class Product(models.Model):

    name = models.CharField(max_length=200)
    created_at = models.DateTimeField(default=datetime.now)
    status = models.CharField(max_length=50,default="Available")
    category = models.ForeignKey(Category, on_delete=models.CASCADE,related_name="products")

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


