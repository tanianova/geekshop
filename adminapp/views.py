from django.shortcuts import render

from authapp.models import User


def index(request):
    return render(request, 'adminapp/index.html')


def admin_users_read(request):
    context = {
        'users': User.objects.all()
    }
    return render(request, 'adminapp/admin-users-read.html', context)
