from django.urls import path

from adminapp import views

app_name = 'adminapp'

urlpatterns = [
    path('', views.index, name='index'),
    path('admin-users-read/', views.UserListView.as_view(), name='admin_users_read'),
    path('admin-users-create/', views.UserCreateView.as_view(), name='admin_users_create'),
    path('admin-users-update/<int:pk>/', views.UserUpdateView.as_view(), name='admin_users_update'),
    path('admin-users-delete/<int:pk>/', views.UserDeleteView.as_view(), name='admin_users_delete'),
    path('admin-products-read/', views.admin_products_read, name='admin_products_read'),
    path('admin-products-create/', views.admin_products_create, name='admin_products_create'),
    path('admin-products-update/<int:id>/', views.admin_products_update, name='admin_products_update'),
    path('admin-products-delete/<int:id>/', views.admin_products_delete, name='admin_products_delete'),

]
