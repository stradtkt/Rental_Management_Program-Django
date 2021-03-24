from django.shortcuts import render, redirect, reverse
from django.contrib.auth.models import User
from django.contrib import messages, auth
from renters.models import Renter, Review

def index(request):
    context = {}
    return render(request, 'accounts/accounts.html', context)

def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request, user)
            messages.success(request, 'You are now logged in!')
            return redirect('pages:home')
        else:
            messages.error(request, 'Invalid Credentials.')
            return redirect('accounts:login')
    else:
        return render(request, 'accounts/login.html')


def register(request):
    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        password2 = request.POST['password2']
        if password == password2:
            if User.objects.filter(username=username).exists():
                messages.error(request, 'Username already exists.')
                return redirect('accounts:register')
            else:
                if User.objects.filter(email=email).exists():
                    messages.error(request, 'Email already exists.')
                    return redirect('accounts:register')
                else:
                    user = User.objects.create_user(
                        username=username,
                        password=password,
                        email=email,
                        first_name=first_name,
                        last_name=last_name,
                    )
                    user.save()
                    messages.success(request, 'You are now registered and can now log in!')
                    return redirect('accounts:login')
        else:
            messages.error(request, 'Passwords do not match!')
    else:
        return render(request, 'accounts/register.html')


def logout(request):
    if request.method == 'POST':
        auth.logout(request)
        messages.success(request, 'You are now logged out!')
        return redirect('home')
    return redirect('home')


def dashboard(request):
    renters = Renter.objects.filter(user_id=request.user.id)
    context = {
        "renters": renters
    }
    return render(request, 'accounts/dashboard.html', context)