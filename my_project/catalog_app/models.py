from django.db import models
from django.urls import reverse


class Category(models.Model):
    name = models.CharField(max_length=200, db_index=True)
    slug = models.SlugField(max_length=200, db_index=True, unique=True)

    class Meta:
        ordering = ('name',)
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

    def get_absolute_url(self):
        return reverse('category', kwargs={'cat_slug': self.slug})
        # return reverse('category:show_category', args=[self.slug])
    
    def __str__(self):
        return self.name
                        

class Product(models.Model):
    category = models.ForeignKey(Category, on_delete  = models.CASCADE, related_name='products')
    # category = models.ForeignKey('Category', on_delete  = models.PROTECT, related_name='products')
    name = models.CharField(max_length=200, db_index=True)
    slug = models.SlugField(max_length=200, db_index=True)
    # slug = models.SlugField(max_length=200, db_index=True, unique=True)
    image = models.ImageField(upload_to='images/', 
                            default='pngtree-super-selling-product-tag-png-image_4477856.png', blank=True)
    description = models.TextField(blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    stock = models.PositiveIntegerField()
    available = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ('name',)
        index_together = (('id', 'slug'),)

    def get_absolute_url(self):
        # return reverse('???', kwargs={'cat_slug': self.slug})
        return reverse('catalog:product_detail', args=[self.id, self.slug])

    def __str__(self):
        return self.name
