from django.contrib.auth.models import Group, User
from rest_framework import permissions, viewsets
from rest_framework.response import Response
from app.serializers import UserSerializer , ArticleSerializer, CategorySerializer, TagSerializer
from app.models import Article, Category, Tag
from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_page


class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    
    
    def get_queryset(self):
        import time
        time.sleep(5)
        return super().get_queryset()
    
    @method_decorator(cache_page(60 * 15,key_prefix='category_list'))     
    def list(self, request):
        return super().list(request)

    
    def retrieve(self, request, pk=None):
        return super().retrieve(request, pk=pk)
    
class TagViewSet(viewsets.ModelViewSet):
    queryset = Tag.objects.all()
    serializer_class = TagSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    
    @method_decorator(cache_page(60 * 15,key_prefix='tag_list'))
    def list(self, request):
        return super().list(request)
    
    def retrieve(self, request, pk=None):
        return super().retrieve(request, pk=pk)