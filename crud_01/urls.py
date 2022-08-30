"""crud_01 URL Configuration

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
from core.views import emprego_listar, emprego_cadastro, emprego_editar, emprego_remover

urlpatterns = [
    path('admin/', admin.site.urls),
    path('emprego/', emprego_listar, name='emprego_listar'),
    path('emprego_cadastro/', emprego_cadastro, name='emprego_cadastro'),
    path('emprego_editar/<int:id>/', emprego_editar, name='emprego_editar'),
    path('emprego_remover/<int:id>/', emprego_remover, name='emprego_remover'),
]
