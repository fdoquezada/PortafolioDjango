"""
URL configuration for Portafolio project.

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
from django.contrib import admin
from django.urls import path, include
from django.shortcuts import redirect
from django.conf.urls import handler404
from error_app.views import error_404

# Primer método
# def redirect_to_home(request):
#     return redirect('home', permanent=True)

urlpatterns = [
    # path('', redirect_to_home),   Primer método
    path('', lambda request: redirect('home', permanent=True)), # Segundo método
    path('admin/', admin.site.urls),
    path('home/', include('Authapp.urls')),
    path('contactame/', include('Contactame.urls')),
    path('database/', include('database.urls')),
    path('queries/', include('queries.urls')),
]

handler404 = 'error_app.views.error_404'
