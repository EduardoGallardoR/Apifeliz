"""APIEDU URL Configuration

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
from api.views import Home 
from api.views import Inicio
from api.views import power
from api.views import Listing
from api.views import Pag2
from api.views import Pag3
from api.views import CheckOut

from api import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('login/', views.login, name='login'),
    path('',Inicio.as_view(),name='index'),
    path('listing/',Listing.as_view(),name='listing'),
    path('pag2/',Pag2.as_view(),name='pag2'),
    path('pag3/',Pag3.as_view(),name='pag3'),
    path('Registro/', views.form_verificado, name='Registro'),
    path('dashboard/', power.as_view(), name='dash'),
    path('payment/', views.CheckOut, name='payment'),
    path('success/', views.success, name='success'),
    path('cancel/', views.cancel, name='cancel'),
]

from django.contrib.staticfiles.urls import staticfiles_urlpatterns # new
urlpatterns += staticfiles_urlpatterns() # new