from django.contrib.auth.decorators import login_required, user_passes_test
from django.shortcuts import render, redirect, get_object_or_404
from apps.reviews.models import Review, Product
from apps.articles.models import Article
from apps.affiliates.models import AffiliateClick
from django.contrib.auth.models import User
from .forms import ProductForm

def admin_only(user):
    return user.is_superuser

@login_required
@user_passes_test(admin_only)
def dashboard(request):
    context = {
        "users": User.objects.count(),
        "products": Product.objects.count(),
        "reviews": Review.objects.count(),
        "articles": Article.objects.count(),
        "clicks": AffiliateClick.objects.count(),
    }
    return render(request, "adminpanel/dashboard.html", context)

# Products 

@login_required
@user_passes_test(admin_only)
def products_list(request):
    products = Product.objects.all()
    return render(request, "adminpanel/products_list.html", {"products": products})

@login_required
@user_passes_test(admin_only)
def product_add(request):
    if request.method == "POST":
        form = ProductForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("adminpanel:admin_products")
    else:
        form = ProductForm()

    return render(request, "adminpanel/product_form.html", {
        "form": form,
        "action": "Add"
    })

@login_required
@user_passes_test(admin_only)
def product_edit(request, pk):
    product = get_object_or_404(Product, pk=pk)

    if request.method == "POST":
        form = ProductForm(request.POST, instance=product)
        if form.is_valid():
            form.save()
            return redirect("adminpanel:admin_products")
    else:
        form = ProductForm(instance=product)

    return render(request, "adminpanel/product_form.html", {
        "form": form,
        "action": "Edit"
    })

@login_required
@user_passes_test(admin_only)
def product_delete(request, pk):
    product = get_object_or_404(Product, pk=pk)

    if request.method == "POST":
        product.delete()
        return redirect("adminpanel:admin_products")

    return render(request, "adminpanel/product_confirm_delete.html", {
        "product": product
    })

# review 
@login_required
@user_passes_test(admin_only)
def reviews_list(request):
    reviews = Review.objects.all()
    return render(request, "adminpanel/reviews_list.html", {"reviews": reviews})

@login_required
@user_passes_test(admin_only)
def review_add(request):
    if request.method == "POST":
        form = ProductForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("adminpanel:admin_products")
    else:
        form = ProductForm()

    return render(request, "adminpanel/product_form.html", {
        "form": form,
        "action": "Add"
    })

@login_required
@user_passes_test(admin_only)
def review_edit(request, pk):
    product = get_object_or_404(Product, pk=pk)

    if request.method == "POST":
        form = ProductForm(request.POST, instance=product)
        if form.is_valid():
            form.save()
            return redirect("adminpanel:admin_products")
    else:
        form = ProductForm(instance=product)

    return render(request, "adminpanel/product_form.html", {
        "form": form,
        "action": "Edit"
    })

@login_required
@user_passes_test(admin_only)
def review_delete(request, pk):
    product = get_object_or_404(Product, pk=pk)

    if request.method == "POST":
        product.delete()
        return redirect("adminpanel:admin_products")

    return render(request, "adminpanel/product_confirm_delete.html", {
        "product": product
    })

@login_required
@user_passes_test(admin_only)
def articles_list(request):
    articles = Article.objects.all()
    return render(request, "adminpanel/articles_list.html", {"articles": articles})


@login_required
@user_passes_test(admin_only)
def users_list(request):
    users = User.objects.all()
    return render(request, "adminpanel/users_list.html", {"users": users})


@login_required
@user_passes_test(admin_only)
def clicks_list(request):
    clicks = AffiliateClick.objects.all()
    return render(request, "adminpanel/clicks_list.html", {"clicks": clicks})