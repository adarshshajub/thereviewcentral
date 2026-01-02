from django.shortcuts import render, get_object_or_404
from .models import Article

def article_list(request):
    articles = Article.objects.filter(published=True)
    return render(request, "articles/article_list.html", {
        "articles": articles
    })


def article_detail(request, slug):
    article = get_object_or_404(Article, slug=slug, published=True)
    products = article.articleproduct_set.all()

    return render(request, "articles/article_detail.html", {
        "article": article,
        "products": products
    })
