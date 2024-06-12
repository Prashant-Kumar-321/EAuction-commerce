from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models.categories import Category 
from .models.user import User
from .models.listings import Listing 


class CategoryAdmin(admin.ModelAdmin): 
	list_display = ('ctg', 'id')

class UserAdmin(UserAdmin): 
	list_display = ("username", "first_name", "last_name", "email", "password")

# Register your models here.

admin.site.register(Category, CategoryAdmin)  
admin.site.register(User, UserAdmin) 
admin.site.register(Listing) 