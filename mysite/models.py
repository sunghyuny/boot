from django.db import models
from django.contrib.auth.models import User
from django.conf import settings
from urllib.parse import urlparse
from django.core.files import File

# Create your models here.
class MainContent(models.Model):
    title = models.CharField(max_length= 200)
    content = models.TextField()
    pub_date=models.DateTimeField('date published')

    def __str__(self):
        return self.title


class Comment(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    content_list = models.ForeignKey(MainContent, on_delete = models.CASCADE)
    content = models.TextField()
    create_date = models.DateTimeField(auto_now_add=True)
    modify_date = models.DateTimeField(auto_now = True)
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)


class Category(models.Model):
    name = models.CharField(max_length=32, verbose_name="카테고리명")
    quantity = models.IntegerField(default=0, verbose_name="수량")

    def __str__(self):
        return self.name

    class Meta:
        db_table = "Shoppingmall_Category"
        verbose_name = "카테고리"
        verbose_name_plural = "카테고리"

class Product(models.Model):
    price = models.IntegerField(verbose_name="상품가격")
    description = models.TextField(verbose_name="상품설명")
    stock = models.IntegerField(verbose_name="재고")
    registered_date = models.DateTimeField(verbose_name="등록시간", auto_now_add=True)
    imgfile = models.ImageField(upload_to="products/", null=True, blank=True, verbose_name="상품이미지")
    name = models.CharField(max_length=32, verbose_name="상품명")
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, related_name='products',
                                 verbose_name="카테고리")

    def save(self, *args, **kwargs):
        # 상품이 저장될 때 카테고리의 수량 업데이트
        if self.category:
            self.category.quantity += 1  # 상품이 추가될 때
            self.category.save()
        super().save(*args, **kwargs)

    def delete(self, *args, **kwargs):
        # 상품이 삭제될 때 카테고리의 수량 업데이트
        if self.category:
            self.category.quantity -= 1  # 상품이 삭제될 때
            self.category.save()
        super().delete(*args, **kwargs)

    def __str__(self):
        return self.name

    class Meta:
        db_table = "Shoppingmall_Product"
        verbose_name = "상품"
        verbose_name_plural = "상품"

