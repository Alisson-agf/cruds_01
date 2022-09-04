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
from django.conf import settings
from django.conf.urls.static import static
from core import views
from core.views import professor_cadastro,professor_editar,professor_listar,professor_remover, home
from core.views import informatica_cadastro, informatica_editar, informatica_listar, informatica_remover
from core.views import motorista_cadastro, motorista_editar, motorista_listar, motorista_remover

urlpatterns = [
    path('admin/', admin.site.urls),

    path('', home, name='home'),
    path('professor_cadastro/',professor_cadastro, name='professor_cadastro'),
    path('professor_editar/',professor_editar, name='professor_editar'),
    path('professor_listar/',professor_listar, name='professor_listar'),
    path('professor_remover/',professor_remover, name='professor_remover'),

    path('informatica_cadastro/',informatica_cadastro, name='informatica_cadastro'),
    path('informatica_editar/',informatica_editar, name='informatica_editar'),
    path('informatica_listar/',informatica_listar, name='informatica_listar'),
    path('informatica_remover/',informatica_remover, name='informatica_remover'),

    path('motorista_cadastro/',motorista_cadastro, name='motorista_cadastro'),
    path('motorista_editar/',motorista_editar, name='motorista_editar'),
    path('motorista_listar/',motorista_listar, name='motorista_listar'),
    path('motorista_remover/',motorista_remover, name='motorista_remover'),




] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
