from django.shortcuts import render, HttpResponseRedirect
from django.urls import reverse

from authapp.models import User
from adminapp.forms import UserAdminRegisterForm, UserAdminProfileForm


def index(request):
    return render(request, 'adminapp/index.html')


def admin_users_read(request):
    context = {
        'users': User.objects.all()
    }
    return render(request, 'adminapp/admin-users-read.html', context)


def admin_users_create(request):
    if request.method == 'POST':
        form = UserAdminRegisterForm(data=request.POST, files=request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('admins:admin_users_read'))
    else:
        form = UserAdminRegisterForm()
    context = {
        'title': 'GeekShop - Регистрация',
        'form': form,
    }
    return render(request, 'adminapp/admin-users-create.html', context)


def admin_users_update(request, id=None):
    user = User.objects.get(id=id)
    if request.method == 'POST':
        form = UserAdminProfileForm(data=request.POST, files=request.FILES, instance=user)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('adminapp:admin_users_read'))
    else:
        form = UserAdminProfileForm(instance=user)
    context = {'form': form, 'current_user': user}
    return render(request, 'adminapp/admin-users-update-delete.html', context)
