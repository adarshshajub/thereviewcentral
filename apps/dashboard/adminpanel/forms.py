from django import forms
from apps.reviews.models import Product, Review


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = [
            "title",
            "description",
            "slug",
            "affiliate_url",
            "brand",
            "category",
            "image",
        ]
        widgets = {
            "title": forms.TextInput(attrs={"class": "form-control"}),
            "description": forms.Textarea(attrs={"rows": 4, "class": "form-control"}),
            "slug": forms.TextInput(attrs={"class": "form-control"}),
            "affiliate_url": forms.TextInput(attrs={"class": "form-control"}),
            "brand": forms.TextInput(attrs={"class": "form-control"}),
            "category": forms.Select(attrs={"class": "form-select"}),
            "image": forms.ClearableFileInput(attrs={'class': 'form-control', 'accept': 'image/*'}),
            

         }


class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = [
            "product",
            "author",
            "slug",
            "title",
            "rating",
            "summary",
            "content",
            "pros",
            "cons",
            "verdict",
            "published",
            "publish_date",
        ]
