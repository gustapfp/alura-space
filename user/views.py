from django.shortcuts import render
from user.forms import LoginForms

# Create your views here.
def login(request):
    form = LoginForms()
    return render(request, 'user/login.html', {"form":form})

def register(request):
    pass
