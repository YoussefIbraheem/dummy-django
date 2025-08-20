from django.shortcuts import render , redirect
from app.models import Article
from django.utils.translation import gettext as _
from app.forms import ArticleForm
import logging

logger = logging.getLogger(__name__)

def article_list(request):
    articles = Article.objects.all()
    
    return render(request, 'app/article_list.html', {'articles': articles})


def article_detail(request, slug):
    article = Article.objects.get(slug=slug)
    
    return render(request, 'app/article_detail.html', {'article': article})

def register_article(request):
    if request.method == "POST":
        form = ArticleForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("article_list")  # Redirect after successful creation
    else:
        form = ArticleForm()
    return render(request, "blog/article_form.html", {"form": form})
