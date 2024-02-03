"""
URL configuration for ChainPro project.

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
from django.urls import path ,include
from ChainApp.views import ChainViewSet, DynamicViewSet
from rest_framework.routers import DefaultRouter
from ChainApp import views

router = DefaultRouter(trailing_slash=False)
router.register(r'chain',ChainViewSet , basename= 'chain')
router.register(r'dynamic',DynamicViewSet , basename= 'get')


urlpatterns = [
    path('admin/', admin.site.urls),
    path('CHAIN/', include(router.urls)),
    path('ChainTEMP' , views.index ),
    path('ChainForm' , views.form )
]