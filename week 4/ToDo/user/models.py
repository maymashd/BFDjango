from django.db import models
from django.contrib.auth.models import AbstractUser, UserManager


# Create your models here.


class MyUser(AbstractUser):
    mobile=models.CharField(max_length=20,blank=True)
    location=models.CharField(max_length=50,blank=True)
    birth_date=models.DateField(null=True,blank=True)
    # MALE = 1
    # FEMALE = 2
    # GENDER = (
    #     (MALE, 'male'),
    #     (FEMALE, 'female'),
    # )
    # gender = models.PositiveSmallIntegerField(choices=GENDER, default=MALE)

    def to_json(self):
        return {
            'id ': self.id,
            'username ': self.username,
            'email ': self.email,
        }
    #
    # @property
    # def price_round(self):
    #     return round(self.price, 3)
    #
    # @classmethod
    # def top_ten(cls):
    #     return cls.objects.all()[:10]
    #
    # @staticmethod
    # def cmp_books(book1, book2):
    #     return book1.price > book2.price





class MyUserManager(UserManager):
    def create_editor(self, username, email=None, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', False)
        extra_fields.setdefault('is_superuser', False)
        extra_fields.setdefault('is_editor', True)
        return self._create_user(username, email, password, **extra_fields)