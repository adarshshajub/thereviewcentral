from django.db import models
from django.contrib.auth.models import User
from apps.reviews.models import Product

class Article(models.Model):
    title = models.CharField(max_length=255)
    slug = models.SlugField(unique=True)
    intro = models.TextField()
    content = models.TextField(blank=True)
    author = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    published = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


class ArticleProduct(models.Model):
    article = models.ForeignKey(Article, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    rank = models.PositiveIntegerField()
    short_note = models.TextField()

    class Meta:
        ordering = ['rank']

    def __str__(self):
        return f"{self.article.title} - {self.product.title}"
