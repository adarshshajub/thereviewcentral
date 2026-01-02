from apps.reviews.models import Review
from apps.articles.models import Article
from apps.affiliates.models import AffiliateClick

def admin_dashboard_context(request):
    return {
        "total_reviews": Review.objects.count(),
        "published_reviews": Review.objects.filter(published=True).count(),
        "total_articles": Article.objects.count(),
        "published_articles": Article.objects.filter(published=True).count(),
        "affiliate_clicks": AffiliateClick.objects.count(),
    }
