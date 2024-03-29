from django.urls import path
from users.views import login, profile, registration, logout, users_cart

app_name = 'users'

urlpatterns = [
    path('login/', login, name='login'),
    path('profile/', profile, name='profile'),
    path('registration/', registration, name='registration'),
    path('users-cart/', users_cart, name='users_cart'),
    path('logout/', logout, name='logout'),
]
