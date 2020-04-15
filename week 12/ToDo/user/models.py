from django.db import models
from django.contrib.auth.models import AbstractUser, UserManager


# Create your models here.


class MyUser(AbstractUser):
    mobile=models.CharField(max_length=20,blank=True)
    location=models.CharField(max_length=50,blank=True)
    birth_date=models.DateField(null=True,blank=True)
    logo=models.ImageField(default='https://lh3.googleusercontent.com/proxy/YjOBOYr3TkjLILcZrpoxJuFb1Qxcbnp31MwHqb4t2AI8gOf1GM3KXdEXn50FXjXRanoo_P-aU1q26AyuGGflMNVyQQJGSyuzu9YHFfir8_Jp7pGBTikouXuSnobauyoSQubJBo7-LL84dszGp-IwSZgzTfz6PoG3BucQulijXLBTuHK1g9extlCN8T1NbEP0b_i-rNl94m8C4s6cd0HguiIBzL1E7qRR8wvGVvZeuy5dtXMqjNCEy40',
                           upload_to='photos/')

    def to_json(self):
        return {
            'id ': self.id,
            'username ': self.username,
            'email ': self.email,
        }






class MyUserManager(UserManager):
    def create_editor(self, username, email=None, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', False)
        extra_fields.setdefault('is_superuser', False)
        extra_fields.setdefault('is_editor', True)
        return self._create_user(username, email, password, **extra_fields)