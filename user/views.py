from django.shortcuts import render, redirect
from user.forms import LoginForms, RegisterForms
from django.contrib import auth

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
                return redirect("index")
            else:
                return redirect("login")

    return render(request, 'user/login.html', {"form":form})

def register(request):
    form = RegisterForms()

    if request.method == "POST":
         form = RegisterForms(request.POST)
         if form.is_valid():
            user_password_1 = form['user_password_1']
            user_password_2 = form['user_password_2']

            if user_password_1 == user_password_2:
                name_user = form['name_login']
                email = form['email']

