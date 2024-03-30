from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, logout,login
from .models import Account 
from .forms import *
from django.contrib.auth.decorators import login_required


# Create your views here.
def home(request):
    user = request.user
    if not user.is_authenticated:
        return redirect('login')
    account = None 
    # Check if the user has an account
    if hasattr(user, 'account'):
        account =Account.objects.get(user=user)
    else:
        return redirect('create-profile')
    return render(request,'home.html',{'account':account,'user':user})


def loginUser(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            print("kch gadbad hai")
            return redirect('login')  # Redirect back to the login page if authentication fails
    else:
        return render(request, 'login.html')


def logoutUser(request):
    logout(request)
    return redirect('login')

def other(request):
    print("Redirected to page")
    return render(request, 'other.html')


@login_required
def create_profile(request):
    form = AccountForm()
    if request.method == 'POST':
        form = AccountForm(request.POST, request.FILES)
        if form.is_valid():
            account = form.save(commit=False)
            account.user = request.user
            account.save()
            return redirect('home')
    context = {'form': form}
    return render(request, 'accountform.html', context)


