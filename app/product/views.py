from django.shortcuts import render, get_object_or_404
from .models import Product, ProductType
from category.models import Category
from cart.forms import CartAddProductForm
# Create your views here.

# def Home(request):
#     return render(request, 'index.html', {})

def product_list(request, category_slug=None):
    category = None
    products =Product.objects.all().filter(available=True)
    if category_slug:
        category = get_object_or_404(Category, slug=category_slug)
        products = products.filter(category=category)
    return render(request,'index.html',{'products': products})


def product_detail(request, id, slug):
    product = get_object_or_404(Product,id=id,slug=slug,available=True)
    cart_form = CartAddProductForm()
    return render(request,'detail.html',{'product': product,'cart_form':cart_form})