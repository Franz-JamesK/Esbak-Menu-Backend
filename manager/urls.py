from django.urls import path
from .views import ManagerRegistration, ManagerLogin,add_food, add_drinks

urlpatterns = [
    path('register/', ManagerRegistration, name='manager-registration'),
    path('login/', ManagerLogin, name='manager-login'),
    path('add-food/', add_food, name='add-food'),
    path('add-drinks/', add_drinks, name='add-drinks'),
]
