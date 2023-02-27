from user.views import login, register, logout
from django.urls import path

urlpatterns = [
    path('login', login, name='login'),
    path('register', register, name='register'),
    path('logout', logout, name='logout')
]