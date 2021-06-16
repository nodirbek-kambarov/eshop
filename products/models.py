from datetime import datetime

import pytz
from ckeditor_uploader.fields import RichTextUploadingField
from django.db import models


class ProductTagModel(models.Model):
    title = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'product tag'
        verbose_name_plural = 'product tags'


class CategoryModel(models.Model):
    title = models.CharField(max_length=20)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'category'
        verbose_name_plural = 'categories'


class BrandModel(models.Model):
    title = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'brand'
        verbose_name_plural = 'brands'


class ProductModel(models.Model):
    title = models.CharField(max_length=100)
    image = models.ImageField(upload_to='products')
    price = models.FloatField()
    discount = models.PositiveIntegerField(default=0)
    short_description = models.TextField()
    long_description = RichTextUploadingField()
    category = models.ForeignKey(
        CategoryModel,
        on_delete=models.PROTECT,
        related_name='products'
    )
    brand = models.ForeignKey(
        BrandModel,
        on_delete=models.PROTECT,
        related_name='products'
    )
    tags = models.ManyToManyField(
        ProductTagModel,
        related_name='products'
    )
    created_at = models.DateTimeField(auto_now_add=True)

    def is_discount(self):
        return self.discount != 0

    def get_price(self):
        if self.is_discount():
            return self.price - self.price * self.discount / 100
        return self.price

    def is_new(self):
        diff = datetime.now(pytz.timezone('Asia/Tashkent')) - self.created_at
        return diff.days <= 3

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'product'
        verbose_name_plural = 'products'
