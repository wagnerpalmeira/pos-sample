from django.shortcuts import render, redirect
from django.contrib.auth import get_user_model, authenticate, login, logout
from django.contrib import messages

def register_user(request):
    if request.method == 'POST':
        user_model = get_user_model()
        email = request.POST['email']
        password = request.POST['password']
        username = request.POST['username']

        user = user_model.objects.create(
            email=email,
            username=username
        )
        user.set_password(password)
        user.save()
        messages.success(request, 'Usuario cadastro com sucesso.')

    return render(request, 'users/register.html')

def login_user(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            return redirect('promotions_view')


    return render(request, 'users/login.html')

def logout_user(request):
    logout(request)
    return redirect('users:login_user')
