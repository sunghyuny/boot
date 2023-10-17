
from django.contrib.auth import login
from django.shortcuts import render,redirect
from accounts.forms import SignupForm

# Create your views here.
def signup(request):
    if request.method == "POST":
        form = SignupForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('/')
    else:
        form=SignupForm()
    return render(request, 'accounts/signup.html', {'form':form})

def agreement(request):
    return render(request, 'accounts/agreement.html')

def find_id(request):
    return render(request, 'accounts/find_id.html')

def find_pw(request):
    return render(request, 'accounts/find_pw.html')