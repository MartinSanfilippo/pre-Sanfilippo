"""
URL configuration for config project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib import admin
from django.urls import path
from servicios import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('login', LoginView.as_view(template_name='servicios/login.html'), name='login'),
    path('', views.index, name="index"),
    path("cliente/list/", views.ClienteList.as_view(), name="cliente_list"),
    path("pedido/list/", views.PedidoList.as_view(), name="pedido_list"),
    path("producto/list/", views.ProductoList.as_view(), name="producto_list"),
    path("cliente/create/", views.cliente_create, name="cliente_create"),
    path("pedido/create/", views.pedido_create, name="pedido_create"),
    path("producto/create/", views.producto_create, name="producto_create"),
    path("producto/detail/<int:pk>", views.producto_detail, name="producto_detail"),
    path("producto/update/<int:pk>", views.producto_update, name="producto_update"),
    path("producto/delete/<int:pk>", views.producto_delete, name="producto_delete"),
    
]
