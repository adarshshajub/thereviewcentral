from django.shortcuts import get_object_or_404, redirect
from apps.reviews.models import Product
from .models import AffiliateClick

def affiliate_redirect(request, slug):
    product = get_object_or_404(Product, slug=slug)
    AffiliateClick.objects.create(product=product)
    return redirect(product.affiliate_url)
