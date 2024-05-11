from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import messages, auth
from contact.forms import RegisterForm, RegisterUpdateForm

def register(request):
    form = RegisterForm()

    if request.method == 'POST':
       form = RegisterForm(request.POST)
       if form.is_valid():
           form.save()
           messages.success(request, 'Usuário cadastrado!')

           return redirect('login')

    return render(request, 'contact/register.html', {'form': form})


def user_update(request):
    form = RegisterUpdateForm(instance=request.user)

    if request.method != 'POST':
        return render(request, 'contact/user_update.html', {'form': form})
    
    form = RegisterUpdateForm(data=request.POST, instance=request.user)

    if not form.is_valid():
        return render(request, 'contact/user_update.html', {'form': form})
    form.save()
    return redirect('user_update')


def login_view(request):
    form = AuthenticationForm(request)

    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)

        if form.is_valid():
            user = form.get_user()
            auth.login(request, user)
            messages.success(request, 'Logado com sucesso!')
            return redirect('index')
        messages.error(request, 'Usuário ou senha inválido!')

    return render(request, 'contact/login.html', {'form': form})


def logout_view(request):
    auth.logout(request)
    return redirect('login')