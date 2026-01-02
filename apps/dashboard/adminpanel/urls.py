from django.urls import path
from . import views 

app_name = 'adminpanel'

urlpatterns = [
    path("", views.dashboard, name="admin_dashboard"),
    path("products/", views.products_list, name="admin_products"),
    path("products/add/", views.product_add, name="admin_product_add"),
    path("products/edit/<int:pk>/", views.product_edit, name="admin_product_edit"),
    path("products/delete/<int:pk>/", views.product_delete, name="admin_product_delete"),
    path("reviews/", views.reviews_list, name="admin_reviews"),
    path("articles/", views.articles_list, name="admin_articles"),
    path("users/", views.users_list, name="admin_users"),
    path("clicks/", views.clicks_list, name="admin_clicks"),
]