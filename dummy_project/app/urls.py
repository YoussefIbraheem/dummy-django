from django.urls import path , include
from app import views

urlpatterns = [
    path('register/', views.register , name='register'),
    path('', views.home, name='home'),
]
