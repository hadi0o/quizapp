from django.urls import path
from .views import Login, Register, profile_view

app_name = 'account'

urlpatterns = [
    path('login', Login.as_view(), name='login_page'),
    path('register', Register.as_view(), name='register_page'),
    path('profile', profile_view, name='profile_page'),
]
