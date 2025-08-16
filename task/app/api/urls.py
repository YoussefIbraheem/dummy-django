from django.urls import path , include
from app.api import views
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'categories', views.CategoryViewSet, basename='category')
router.register(r'tags', views.TagViewSet, basename='tag')

urlpatterns = [
    path('',include(router.urls)),
]
