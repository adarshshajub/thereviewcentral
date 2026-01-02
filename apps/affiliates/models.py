from django.db import models
from apps.reviews.models import Product

class AffiliateClick(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    ip_address = models.GenericIPAddressField()
    clicked_at = models.DateTimeField(auto_now_add=True)
