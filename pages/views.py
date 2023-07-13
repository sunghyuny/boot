from django.shortcuts import render

# Create your views here.

def mainpage(request):
    return render(request, 'pages/mainpage.html')

def company (request):
    return render(request, 'pages/company_info.html')

def home(request):
    return render(request, 'pages/home.html')

def login(request):
    return render(request, 'pages/login.html')

