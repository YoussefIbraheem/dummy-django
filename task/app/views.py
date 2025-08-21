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
    article = Article.objects.filter(slug=slug).first()
    article.view_count += 1
    article.save()    
    return render(request, 'app/article_detail.html', {'article': article})

def register_article(request):
    if request.method == 'POST':
        form = ArticleForm(request.POST)
        if form.is_valid():
            title = form.cleaned_data['title']
            content = form.cleaned_data['content']
            author = form.cleaned_data['author']
            
            article = Article(title=title, content=content, author=author)
            article.save()
            
            logger.info(f"Article '{title}' created successfully.")
            return redirect('home')
    else:
        form = ArticleForm()
    
    return render(request, 'app/article_form.html', {'form': form})
