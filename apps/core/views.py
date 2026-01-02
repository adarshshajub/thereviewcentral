from django.shortcuts import render
from apps.reviews.models import Review

def home(request):
    reviews = Review.objects.filter(published=True)
    return render(request, "core/home.html", {"reviews": reviews})