from django.shortcuts import render
from app.models import Article
from django.utils.translation import gettext as _

def article_list(request):
    articles = Article.objects.all()
    
    return render(request, 'app/article_list.html', {'articles': articles})


def article_detail(request, slug):
    article = Article.objects.get(slug=slug)
    
    return render(request, 'app/article_detail.html', {'article': article})



