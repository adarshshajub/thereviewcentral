from django.contrib import admin
from .models import Category, Product, Review

@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ('title', 'product', 'rating', 'published')
    prepopulated_fields = {"slug": ("title",)}
    list_filter = ('published', 'rating')


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'brand', 'category')
    prepopulated_fields = {"slug": ("title",)}


@admin.register(Category)
class CategroyAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug')
    prepopulated_fields = {"slug": ("name",)}
