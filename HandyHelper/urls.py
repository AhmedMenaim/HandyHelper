"""HandyHelper URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from HandyHelperDjango.views import Dashboard

from Users.views import (
    registeration_view,
    logout_view,
    login_view,
)
from HandyHelperDjango.views import (
    Dashboard,
)

urlpatterns = [
    path('', include('HandyHelperDjango.urls')),
    path('', Dashboard, name="Dashboard" ),
    path('admin/', admin.site.urls),
    path('Job/', include('Job.urls', 'Job')),

    path('Register', registeration_view, name='Register'),
    path('Logout',logout_view,name="Logout"),
    path('Login',login_view,name="Login"),
]
