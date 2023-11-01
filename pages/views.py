from django.shortcuts import render
from mysite.models import Product
# Create your views here.

def mainpage(request):
    products= Product.objects.order_by('registered_date')

    return render(request, 'pages/mainpage.html', {'products':products})

def company (request):
    return render(request, 'pages/company_info.html')

def home(request):
    return render(request, 'pages/home.html')

def login(request):
    return render(request, 'pages/login.html')

