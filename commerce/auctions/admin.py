from django.contrib import admin
from .models.categories import Category 
from .models.user import User


class CategoryAdmin(admin.ModelAdmin): 
	list_display = ('ctg', 'id')

# Register your models here.

admin.site.register(Category, CategoryAdmin)  
admin.site.register(User) 