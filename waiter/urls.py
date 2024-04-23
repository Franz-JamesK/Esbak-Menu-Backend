from django.urls import path
from .views import register_waiter, login_waiter

urlpatterns = [
    path('register/', register_waiter, name='register-waiter'),
    path('login/', login_waiter, name='login-waiter'),
]
