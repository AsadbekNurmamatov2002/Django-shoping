from django.shortcuts import render, get_object_or_404
from .models import Product
from category.models import Category
from cart.forms import CartAddProductForm
from django.db.models import Q
# Create your views here.

# def Home(request):
#     return render(request, 'index.html', {})

def product_list(request, category_slug=None):
    q=request.GET.get('q') if request.GET.get('q') !=None else ""
    category = None
    products =Product.objects.all().filter(Q(available=True) |
                                           Q(name__icontains=q) |
                                           Q(category__name__icontains=q) |
                                           Q(description__icontains=q)).order_by('-updated', "-created")
    if category_slug:
        category = get_object_or_404(Category, slug=category_slug)
        products = products.filter(category=category)
    cart_form = CartAddProductForm()
    return render(request,'index.html',{'products': products, "cart_form":cart_form})


def product_detail(request, id, slug):
    products = get_object_or_404(Product,id=id,slug=slug,available=True)
    cart_form = CartAddProductForm()
    return render(request,'product/product.html',{'products': products,'cart_form':cart_form})