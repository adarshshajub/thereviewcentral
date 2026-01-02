from django.urls import path
from .views import affiliate_redirect

urlpatterns = [
    path("go/<slug:slug>/", affiliate_redirect, name="affiliate_redirect"),
]
