from django import forms
from django.forms import ModelForm
from business.models import Products


class ProductsAddForm(ModelForm):
    class Meta:
        model=Products
        fields=['product_name','product_image','price','discount_price','category','description']
