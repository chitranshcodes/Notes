from django.urls import path
from . import views

app_name='notes'

urlpatterns = [
    path('', views.home, name='home'),
    path('login/', views.Login, name='login'),
    path('register/', views.register, name='register'),
    path('about/', views.about, name='about'),
]
