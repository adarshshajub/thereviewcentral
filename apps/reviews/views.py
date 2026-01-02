from django.shortcuts import render, get_object_or_404
from .models import Review

def review_detail(request, slug):
    review = get_object_or_404(
        Review,
        slug=slug,
        published=True
    )
    return render(
        request,
        "reviews/review_detail.html",
        {"review": review}
    )
