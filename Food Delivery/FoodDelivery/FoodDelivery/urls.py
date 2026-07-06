"""
URL configuration for FoodDelivery project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.0/topics/http/urls/
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
from Orders import views as order_views
from Restaurants import views as restaurant_views
from Menu import views as menu_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('orders/', order_views.index, name='order_index'),
    path('restaurants/', restaurant_views.index, name='restaurant_index'),
    path('menu/', menu_views.index, name='menu_index')
]
