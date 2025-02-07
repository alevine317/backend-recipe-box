"""recipebox URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

from recipebox.views import *
from recipebox.models import Author, Recipe

# admin.site.register(Author)
# admin.site.register(Recipe)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name='homepage'),
    path('author/', author, name='id'),
    path('recipe/', recipe, name='id'),
    path('addrecipe/', addrecipe),
    path('register/', register, name='register'),
    path('login/', login_view, name='login_view'),
    path('logout', logout_user, name='logout'),
    path('editrecipe/<int:id>/', editrecipe, name='editrecipe'),
]
