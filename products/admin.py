from django.contrib import admin
from .models import Product, Test



class Products_Admin(admin.ModelAdmin):

    list_display = ['name', 'price', 'condition', 'category']
    list_display_links = ['name']
    list_editable = ['price', 'category', 'condition']
    search_fields = ['name']
    list_filter = ['category', 'price']
    fields = ['name', 'price', 'condition']



admin.site.register(Product, Products_Admin)
admin.site.register(Test)
