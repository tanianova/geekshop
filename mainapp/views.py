from django.shortcuts import render

from mainapp.models import product, ProductCategory
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


def index(request):
    context = {
        'title': 'Geekshop',
    }
    return render(request, 'mainapp/index.html', context)


def products(request, category_id=None, page=1):
    if category_id:
        products = product.objects.filter(category_id=category_id)
    else:
        products = product.objects.all()
    per_page = 3
    paginator = Paginator(products.order_by('-price'), per_page)
    try:
        products_paginator = paginator.page(page)
    except PageNotAnInteger:
        products_paginator = paginator.page(1)
    except EmptyPage:
        products_paginator = paginator.page(paginator.num_pages)
    context = {
        'title': 'GeekShop - Каталог',
        'products': products_paginator,
        'categories': ProductCategory.objects.all(),
    }
    return render(request, 'mainapp/products.html', context)
