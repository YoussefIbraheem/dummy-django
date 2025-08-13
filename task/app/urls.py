from django.urls import path
from app.views import article_list



urlpatterns = [
    path('articles/', article_list),
]
