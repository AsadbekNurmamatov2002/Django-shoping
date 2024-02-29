from .models import Category

def CategoryA(request):
    return {'category':Category.objects.all().order_by('-id')}