from django.db import models
from django.urls import reverse
from django.utils.text import slugify
# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200, unique=True)
    image=models.ImageField(upload_to='category/%Y/%M/%D/')
    class Meta:
        ordering = ['name']
        indexes = [
            models.Index(fields=['name']),
        ]
        verbose_name = 'category'
        verbose_name_plural = 'categories'
    def __str__(self):
       return self.name
    def save(self, *args, **kwargs):
        if self.slug==None:
            slug = slugify(self.name)
            has_slog=Category.objects.filter(slug=slug).exists()
            count=1
            while has_slog:
                count+=1
                slug=slugify(self.name)+'-'+str(count)
                has_slog=Category.objects.filter(slug=slug).exclude()
            self.slug=slug
        super().save(*args, **kwargs)
    def get_absolute_url(self):
        return reverse('shop:product_list_by_category',args=[self.slug])