from django.contrib import admin

from products.models import CategoryModel, ProductTagModel, BrandModel, ProductModel


@admin.register(CategoryModel)
class CategoryModelAdmin(admin.ModelAdmin):
    list_display = ['title', 'created_at']
    search_fields = ['title']
    list_filter = ['created_at']


@admin.register(ProductTagModel)
class ProductTagModelAdmin(admin.ModelAdmin):
    list_display = ['title', 'created_at']
    search_fields = ['title']
    list_filter = ['created_at']


@admin.register(BrandModel)
class BrandModelAdmin(admin.ModelAdmin):
    list_display = ['title', 'created_at']
    search_fields = ['title']
    list_filter = ['created_at']


@admin.register(ProductModel)
class ProductModelAdmin(admin.ModelAdmin):
    list_display = ['title', 'short_description', 'price', 'discount', 'category', 'brand', 'created_at']
    list_filter = ['category', 'brand', 'tags', 'created_at']
    search_fields = ['title', 'short_description']
    autocomplete_fields = ['category', 'brand', 'tags']
