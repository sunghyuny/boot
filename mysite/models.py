from django.db import models
from django.contrib.auth.models import User
from django.conf import settings
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


class Product(models.Model):
    price = models.IntegerField(verbose_name="상품가격")
    description = models.TextField(verbose_name="상품설명")
    stock = models.IntegerField(verbose_name="재고")
    registered_date = models.DateTimeField(verbose_name="등록시간", auto_now_add=True)
    imgfile = models.ImageField(upload_to="products/", null=True, blank=True, verbose_name="상품이미지")

    name = models.CharField(max_length=32, verbose_name="상품명")

    def __str__(self):
        return self.name

    class Meta:
        db_table = "Shoppingmall_Product"
        verbose_name = "상품"
        verbose_name_plural = "상품"
