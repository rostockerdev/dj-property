from django.shortcuts import render, redirect
from django.contrib import messages, auth
from django.contrib.auth.models import User


def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request, user)
            messages.success(request, 'You are logged in.')
            return redirect('accounts:dashboard')

        else:
            messages.error(request, 'Invalid Credientials')
            return redirect('accounts:login')
    
    else:
        return render(request, 'accounts/login.html')