from django.urls import path
from . import views

urlpatterns = [
    path('Dashboard', views.Dashboard, name="Dashboard"),
    path('ViewJob',views.ViewJob)
]