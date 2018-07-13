from django.shortcuts import render
from .models import Product

# Create your views here.

def product_list(request):
    products = Product.objects.order_by("created_date")

    return render(request,"shop/product_list.html", {"products": products})