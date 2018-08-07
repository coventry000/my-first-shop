from django.shortcuts import render
from .models import Product
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator

from django.db.models import Q

# for searching

import operator
from django.db.models import Q


# Create your views here.

def product_list(request):
    product_list = Product.objects.order_by("created_date")
    paginator = Paginator(product_list, 6)

    page = request.GET.get("page", 1)
    products = paginator.page(page)
    return render(request,"shop/product_list.html", {"products": products})

def search(request):
    template = "shop/product_list.html"

    query = request.GET.get('q')

    if query:
        results = Product.objects.filter(Q(title__icontains=query))
    else:
        results = Product.objects.all()
    paginator = Paginator(results, 1)


    page = request.GET.get("page", 1)
    products = paginator.page(page)

    return render(request, template, {"products": products, "query": query})






