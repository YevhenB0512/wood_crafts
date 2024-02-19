from django.contrib import auth, messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.urls import reverse

from users.forms import UserLoginForm, UserRegistrationForm, UserProfileForm


def login(request):
    if request.method == 'POST':
        form = UserLoginForm(data=request.POST)
        if form.is_valid():
            username = request.POST['username']
            password = request.POST['password']
            user = auth.authenticate(username=username, password=password)
            if user:
                auth.login(request, user)
                messages.success(request, f'{username}, Вы вошли в аккаунт ')
                return redirect(reverse('main:index'))
    else:
        form = UserLoginForm()

    context = {
        'title': 'Wood crafts - Авторизация',
        'form': form
    }
    return render(request, 'users/login.html', context)


def registration(request):
    if request.method == 'POST':
        form = UserRegistrationForm(data=request.POST)
        if form.is_valid():
            form.save()
            user = form.instance
            auth.login(request, user)
            messages.success(request, f'{user.username}, Вы успешно зарегистрированы ')
            return redirect(reverse('main:index'))
    else:
        form = UserRegistrationForm()
    context = {
        'title': 'Wood crafts - Регистрация',
        'form': form
    }
    return render(request, 'users/registration.html', context)


@login_required
def profile(request):
    if request.method == 'POST':
        form = UserProfileForm(data=request.POST, instance=request.user, files=request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, f'Профиль обновлен')
            return redirect(reverse('user:profile'))
    else:
        form = UserProfileForm(instance=request.user)
    context = {
        'title': 'Wood crafts - Кабинет',
        'form': form
    }
    return render(request, 'users/profile.html', context)


@login_required
def logout(request):
    messages.success(request, f'Вы вышли из аккаунта ')
    auth.logout(request)
    return redirect(reverse('main:index'))
