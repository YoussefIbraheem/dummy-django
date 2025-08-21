from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
from app.factories import ArticleFactory, AuthorFactory
from app.models import Article, Author, Category, Tag

import logging

logger = logging.getLogger(__name__)


class Command(BaseCommand):
    help = "Seed the database with articles"

    def handle(self, *args, **options):
        article_factory = ArticleFactory()
        for _ in range(5):
            if not Author.objects.exists():
                self.stdout.write(
                    self.style.WARNING("No authors found. Please seed authors first.")
                )
                return
            else:
                author = Author.objects.order_by("?").first()
            if not Tag.objects.exists():
                self.stdout.write(
                    self.style.WARNING("No tags found. Please seed tags first.")
                )
                return
            else:
                tags = Tag.objects.order_by("?")[:3]

            if not Category.objects.exists():
                self.stdout.write(
                    self.style.WARNING(
                        "No categories found. Please seed categories first."
                    )
                )
                return
            else:
                category = Category.objects.order_by("?").first()

            article_data = article_factory.create(
                author=author, category=category
            )
            article = Article.objects.create(**article_data)
            article.tags.set(tags)
            article.save()
            logger.info(f"Article '{article.title}' created successfully.")
            self.stdout.write(
                self.style.SUCCESS(f"Successfully created articles under author {author.user.first_name} {author.user.last_name}")
            )
