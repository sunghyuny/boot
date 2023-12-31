from django.shortcuts import render
from mysite.models import Product
from django.db.models import Q
from templates import search_app
# Create your views here.


def searchResult(request):
    products =None
    query =None
    if 'q' in request.GET:
        query = request.GET.get('q')
        products = Product.objects.all().filter(Q(name__contains=query)|Q(description__contains=query))
    return render(request , 'search_app/search.html' , {'query':query, 'products':products})