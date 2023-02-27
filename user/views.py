from django.shortcuts import render, redirect
from user.forms import LoginForms, RegisterForms
from django.contrib import auth, messages
from django.contrib.auth.models import User

# Create your views here.
def login(request):
    form = LoginForms()
    
    if request.method == "POST":
        form = LoginForms(request.POST)
        if form.is_valid():
            name_user = form['name_login'].value()
            user_password = form['user_password'].value()

            user_log = auth.authenticate(
                request, 
                username = name_user,
                password= user_password
            )
            if user_log is not None:
                auth.login(request, user_log)
                messages.success(request, f'{name_user} logado com sucesso!')
                return redirect("index")
            else:
                messages.error(request, 'Erro ao efetuar login')
                return redirect("login")

    return render(request, 'user/login.html', {"form":form})

def register(request):
    form = RegisterForms()

    if request.method == "POST":
         form = RegisterForms(request.POST)
         if form.is_valid():
            if form["user_password_1"].value() != form["user_password_2"].value():
                messages.error(request, 'Senhas não são iguais')
                return redirect('register')
            
            name_user = form['name_login'].value()
            email = form['email'].value()
            user_password = form['user_password_1'].value()


            if User.objects.filter(username=name_user).exists():
                messages.error(request, 'Usuário já existente')
                return redirect('register')
            
            registered_used = User.objects.create_user(
                username = name_user,
                email = email,
                password = user_password
            )
            registered_used.save()
            return redirect('login')
           
    return render(request, 'user/register.html', {"form": form})


def logout(request):
    auth.logout(request)
    messages.success(request, "Logout efetuado com sucesso")
    return redirect('login')