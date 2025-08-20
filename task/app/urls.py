from django.urls import path
from app.views import article_list , article_detail , register_article



urlpatterns = [
    path('articles/<slug:slug>/', article_detail, name='article_detail'),
    path('new-article/', register_article, name='register_article'),
    path('', article_list, name='home'),
]
