from django.contrib import admin
from main.models import MyUser,Category,Product,Order
# Register your models here.

admin.site.register(MyUser)
admin.site.register(Category)
admin.site.register(Product)
admin.site.register(Order)