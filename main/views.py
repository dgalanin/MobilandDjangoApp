from django.shortcuts import render

from .models import Products


def index(request):
    return render(request, 'main/index.html')


def about(request):
    return render(request, 'main/about.html')


def repair(request):
    return render(request, 'main/repair.html')


def store(request):
    products = Products.objects.order_by("-id")
    return render(request, 'main/store.html', {"products": products})
