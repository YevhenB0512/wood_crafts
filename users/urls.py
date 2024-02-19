from django.urls import path
from users.views import login, profile, registration, logout

app_name = 'users'

urlpatterns = [
    path('login/', login, name='login'),
    path('profile/', profile, name='profile'),
    path('registration/', registration, name='registration'),
    path('logout/', logout, name='logout'),
]
