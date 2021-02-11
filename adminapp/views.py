from django.shortcuts import render, HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth.decorators import user_passes_test

from authapp.models import User
from adminapp.forms import UserAdminRegisterForm, UserAdminProfileForm, ProductAdminCreateForm, ProductAdminUpdateForm
from mainapp.models import product


@user_passes_test(lambda u: u.is_superuser, login_url='/')
def index(request):
    return render(request, 'adminapp/index.html')


@user_passes_test(lambda u: u.is_superuser)
def admin_users_read(request):
    context = {
        'users': User.objects.all()
    }
    return render(request, 'adminapp/admin-users-read.html', context)


@user_passes_test(lambda u: u.is_superuser)
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


@user_passes_test(lambda u: u.is_superuser)
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


@user_passes_test(lambda u: u.is_superuser)
def admin_users_delete(request, id=None):
    user = User.objects.get(id=id)
    user.is_active = False
    user.save()
    return HttpResponseRedirect(reverse('admins:admin_users_read'))


def admin_products_read(request):
    context = {'products': product.objects.all()}
    return render(request, 'adminapp/admin-products-read.html', context)


def admin_products_create(request):
    if request.method == 'POST':
        form = ProductAdminCreateForm(data=request.POST, files=request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('admins:admin_products_read'))
    else:
        form = ProductAdminCreateForm()
    context = {'form': form}
    return render(request, 'adminapp/admin-products-create.html', context)


def admin_products_update(request, id=None):
    current_product = product.objects.get(id=id)
    if request.method == 'POST':
        form = ProductAdminUpdateForm(data=request.POST, files=request.FILES, instance=current_product)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('adminapp:admin_products_read'))
    else:
        form = ProductAdminUpdateForm(instance=current_product)
    context = {
        'form': form,
        'current_product': current_product
    }
    return render(request, 'adminapp/admin-products-update-delete.html', context)


def admin_products_delete(request, id=None):
    current_product = product.objects.get(id=id)
    current_product.delete()
    return HttpResponseRedirect(reverse('admins:admin_products_read'))
