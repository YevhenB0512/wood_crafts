from django.shortcuts import render, get_object_or_404, get_list_or_404
from .models import Categories, Products
from django.core.paginator import Paginator


def catalog(request, category_slug):
    page = request.GET.get('page', 1)

    if category_slug == 'vse-tovary':
        goods = Products.objects.all()
    else:
        goods = get_list_or_404(Products.objects.filter(category__slug=category_slug))

    paginator = Paginator(goods, 6)
    current_page = paginator.page(int(page))

    context = {
        'title': 'Wood crafs - Каталог',
        'goods': current_page,
        'slug_url': category_slug
    }
    return render(request, 'goods/catalog.html', context)


def product(request, product_slug):
    product = Products.objects.get(slug=product_slug)
    context = {
        'product': product
    }
    return render(request, 'goods/product.html', context)