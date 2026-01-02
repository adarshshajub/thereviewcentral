from django.contrib.auth.decorators import login_required, user_passes_test
from django.shortcuts import render
from apps.reviews.models import Review
from apps.articles.models import Article

def staff_check(user):
    return user.is_staff or user.is_superuser

@login_required
@user_passes_test(staff_check)
def staff_dashboard(request):
    reviews = Review.objects.filter(author=request.user)
    articles = Article.objects.filter(author=request.user)

    return render(request, "staff/dashboard.html", {
        "reviews": reviews,
        "articles": articles
    })
