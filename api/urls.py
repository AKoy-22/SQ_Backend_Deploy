from django.urls import path

from .import views

urlpatterns = [
    path('', views.getData),
    path('add-user/', views.addUser),
    path('login/', views.loginAuth)
]