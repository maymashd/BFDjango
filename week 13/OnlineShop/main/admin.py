from main.models import MyUser, Category, Product, Order, Notification
from django.contrib import admin

@admin.register(MyUser)
class MyUserAdmin(admin.ModelAdmin):
    list_display = ('id', 'first_name', 'last_name', 'email')

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'created_at', 'status')

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'created_at', 'status','category')

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('id', 'created_at', 'created_by','quantity')

admin.site.register(Notification)