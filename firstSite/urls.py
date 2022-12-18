"""firstSite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from myapp.views import test
from myapp.views import start
from myapp.views import divan
from myapp.views import table
from myapp.views import divanCard
from myapp.views import reg
from myapp.views import table
urlpatterns = [
    path('admin/', admin.site.urls),
    path('test/', test),
    path('start/', start),
    path('divan/', divan),
    path('table/', table),
    path('divan/<int:post_id>', divanCard),
    path('reg/', reg),
    
]
