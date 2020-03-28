from .forms import RegisterForm, LoginForm
from django.contrib.auth.models import User
from django.shortcuts import (
    render, 
    redirect, 
    reverse, 
    HttpResponse)

from django.contrib.auth import (
    login, 
    logout, 
    authenticate, 
    get_user_model)



def register_view(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('name')
            password = form.cleaned_data.get('password')
            email = form.cleaned_data.get('email')
            User.objects.create_user('john', 'lennon@thebeatles.com', 'johnpassword')
            username = 'john'
            password = 'johnpassword'
            user = authenticate(username=username, password=password)
            login(request, user)
            return redirect(reverse('blog:post_list'))

    form = RegisterForm()
    context = {
        'form': form,
    }
    return render(request, 'accounts/register.html', context)


def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            login(request, user)
            return redirect(reverse('blog:post_list'))
    form = LoginForm()
    context = {
        'form': form
    }
    return render(request, 'accounts/login.html', context)


def logout_view(request):
    logout(request)
    return redirect(reverse('blog:post_list'))