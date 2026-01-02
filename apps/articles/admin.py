from django.contrib import admin
from .models import Article, ArticleProduct

class ArticleProductInline(admin.TabularInline):
    model = ArticleProduct
    extra = 1

@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ('title', 'published', 'created_at')
    prepopulated_fields = {"slug": ("title",)}
    inlines = [ArticleProductInline]