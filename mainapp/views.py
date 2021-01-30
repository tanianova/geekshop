from django.shortcuts import render

from mainapp.models import product, ProductCategory


def index(request):
    context = {
        'title': 'Geekshop',
    }
    return render(request, 'mainapp/index.html', context)


def products(request, id=None):
    context = {
        'title': 'GeekShop - Каталог',
        'products': product.objects.all(),
        'categories': ProductCategory.objects.all(),
    }
    return render(request, 'mainapp/products.html', context)
