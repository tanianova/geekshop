from django.urls import path

from authapp.views import login, register, logout, edit

app_name = 'authapp'

urlpatterns = [
    path('login/', login, name='login'),
    path('register/', register, name='register'),
    path('logout/', logout, name='logout'),
    path('edit/', edit, name='edit'),
]
