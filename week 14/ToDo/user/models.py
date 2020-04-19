from django.db import models
from django.contrib.auth.models import AbstractUser, UserManager


# Create your models here.


class MyUser(AbstractUser):
    logo=models.ImageField(default='https://lh3.googleusercontent.com/proxy/YjOBOYr3TkjLILcZrpoxJuFb1Qxcbnp31MwHqb4t2AI8gOf1GM3KXdEXn50FXjXRanoo_P-aU1q26AyuGGflMNVyQQJGSyuzu9YHFfir8_Jp7pGBTikouXuSnobauyoSQubJBo7-LL84dszGp-IwSZgzTfz6PoG3BucQulijXLBTuHK1g9extlCN8T1NbEP0b_i-rNl94m8C4s6cd0HguiIBzL1E7qRR8wvGVvZeuy5dtXMqjNCEy40',
                           upload_to='photos/')



class MyUserProfile(models.Model):
    user=models.ForeignKey(MyUser,on_delete=models.CASCADE,related_name="profile")
    mobile = models.CharField(max_length=20, blank=True)
    location = models.CharField(max_length=50, blank=True)
    birth_date = models.DateField(null=True, blank=True)