"""
URL configuration for products project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.contrib import admin
from django.urls import path
from productapp.views import CategoryCreateView,ProductCreateView,product_list,ProductDetailView,ProductUpdateView,remove_product

urlpatterns = [
    path('admin/', admin.site.urls),
    path('category/add',CategoryCreateView.as_view(),name="category-add"),
    path('product/add',ProductCreateView.as_view(),name="product-add"),
    path('product/all',product_list,name="product-list"),
    path('product/<int:pk>',ProductDetailView.as_view(),name="product-detail"),
    path('product/<int:pk>/change',ProductUpdateView.as_view(),name="product-change"),
    path('product/<int:pk>/remove/',remove_product,name="product-remove"),
    
]
