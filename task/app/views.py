from django.shortcuts import render
from app.models import Article
from django.utils.translation import gettext as _
import logging

logger = logging.getLogger(__name__)

def article_list(request):
    articles = Article.objects.all()
    if not articles:
        logger.warning(_("No articles found in the database."))
    else:
        logger.info(f"Fetched articles from the database.").format( articles.count() )
        
        
    logger.info("Rendering article list view.")
    
    return render(request, 'app/article_list.html', {'articles': articles})


def article_detail(request, slug):
    article = Article.objects.get(slug=slug)
    
    return render(request, 'app/article_detail.html', {'article': article})



