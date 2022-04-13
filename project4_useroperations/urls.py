"""project4_useroperations URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from app4 import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('save_user/', views.saveUsername, name="save_user"),
    path('check_password/', views.checkPassword, name="check_password"),
    path('check_username/', views.checkUsername, name="check_username"),
    path('view_products/',views.viewProducts, name="view_products"),
]
