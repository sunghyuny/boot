from django.contrib import admin
from .models import MainContent,Comment,Product
# Register your models here.


class  MainContentAdmin(admin.ModelAdmin):
    list_display = ['title','content', 'pub_date']
    search_fields=['title']

class CommentAdmin(admin.ModelAdmin):
    list_display = ['content_list', 'content','author','create_date','modify_date']
    search_fields = ['author']


admin.site.register(MainContent,MainContentAdmin)
admin.site.register(Comment, CommentAdmin)

class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'category')

admin.site.register(Product, ProductAdmin)

