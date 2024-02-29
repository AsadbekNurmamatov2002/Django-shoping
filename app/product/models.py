from django.db import models
from django.urls import reverse
from django.utils.text import slugify
from category.models import Category
# from category.models import MainCategory, Category
# Create your models here.


class ProductType(models.Model):
    name=models.CharField(max_length=250, help_text="product turini belgilang masalan--> Bugungi maxsulot yoke eng yahshi maxsulot!!")
CHEGIRMA= ( 
    ("5", "5"), 
    ("7", "7"), 
    ("9", "9"), 
    ("10", "10"), 
    ("12", "12"), 
    ("15", "15"), 
    ("20", "20"), 
    ("25", "25"),
    ("30", "30"),
    ("35","35"),
    ("40","40"),
    ("45","45"), 
    ("50","50"),
)
class Product(models.Model):
    producttype=models.ForeignKey(ProductType,on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, null=True)
    name = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200)
    image = models.FileField(upload_to='products/%Y/%m/%d',blank=True)
    image2 = models.FileField(upload_to='products/%Y/%m/%d',blank=True)
    description = models.TextField(blank=True)
    price = models.DecimalField(max_digits=10,decimal_places=2)
    old_price = models.DecimalField(max_digits=10,decimal_places=2, null=True)
    soni=models.IntegerField(help_text='Maxsulotlar sonu!', null=True)
    available = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    chegirma = models.CharField( max_length = 20, choices = CHEGIRMA, default = '5') 
    class Meta:
        ordering = ['name']
        indexes = [
            models.Index(fields=['id', 'slug']),
            models.Index(fields=['name']),
            models.Index(fields=['-created']),
        ]
    def __str__(self):
        return self.name
    def save(self, *args, **kwargs):
        if self.slug==None:
            slug = slugify(self.nameproduct)
            has_slog=Product.objects.filter(slug=slug).exists()
            count=1
            while has_slog:
                count+=1
                slug=slugify(self.name)+'-'+str(count)
                has_slog=Product.objects.filter(slug=slug).exclude()
            self.slug=slug
        super().save(*args, **kwargs)
    def get_absolute_url(self):
        return reverse("product:Productdatile", args=[self.slug])

class ProductCollor(models.Model):
    product=models.ForeignKey(Product, on_delete=models.CASCADE)
    color=models.CharField(max_length=200, default='#fffff')
    def __str__(self) -> str:
        return self.color
      
def product_galary(instanse, filename):
    return f"product/{instanse.product.slug}/qushimcha/{filename}"

class Rasimlar(models.Model):
    product=models.ForeignKey(Product, on_delete=models.CASCADE)
    file=models.FileField(upload_to=product_galary)
    created=models.DateTimeField(auto_now_add=True)
    updated=models.DateTimeField(auto_now=True)

class Size(models.Model):
    product=models.ForeignKey(Product,on_delete=models.CASCADE)
    size=models.CharField(max_length=100)
    def __str__(self) -> str:
        return self.size
    

    













