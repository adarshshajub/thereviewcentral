from django.db import models
from django.contrib.auth import get_user_model
from django.urls import reverse

User = get_user_model()

class Category(models.Model):
    name = models.CharField(max_length=120)
    slug = models.SlugField(unique=True)

    def __str__(self):
        return self.name


class Product(models.Model):
    title = models.CharField(max_length=255)
    slug = models.SlugField(unique=True)
    brand = models.CharField(max_length=120)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True)
    description = models.TextField()
    image = models.ImageField(upload_to='products/')
    affiliate_url = models.URLField()
    created_at = models.DateTimeField(auto_now_add=True)

    def get_absolute_url(self):
        return reverse('product_detail', args=[self.slug])


class Review(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    author = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    title = models.CharField(max_length=255)
    slug = models.SlugField(unique=True)
    rating = models.DecimalField(max_digits=3, decimal_places=1)
    summary = models.TextField()
    content = models.TextField()
    pros = models.TextField()
    cons = models.TextField()
    verdict = models.TextField()
    published = models.BooleanField(default=False)
    publish_date = models.DateTimeField(null=True, blank=True)

    def get_absolute_url(self):
        return reverse('review_detail', args=[self.slug])
