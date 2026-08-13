from django.shortcuts import render
from .models import Product

def product(request):

    return render(request, 'products/product.html')

def products(request):

    return render(request, 'products/products.html', {'prod' : Product.objects.all().exclude(price__gte=1000)} )