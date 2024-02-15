from django.shortcuts import render


def index(request):
    context = {
        'title': 'Wood crafts - Главная',
        'content': 'Wood crafts store'
    }
    return render(request, 'main/index.html', context)


def about(request):
    context = {
        'title': 'Wood crafts - О нас',
        'content': 'О нас'
    }
    return render(request, 'main/about.html', context)