from django.core.management.base import BaseCommand , CommandError
from app.models import Category
from app.factories import CategoryFactory

class Command(BaseCommand):
    help = 'Seed categories into the database'

    def handle(self, *args, **kwargs):
        factory = CategoryFactory()
        for _ in range(10):
            category_data = factory.create()
            Category.objects.create(**category_data)
        self.stdout.write(self.style.SUCCESS('Successfully seeded categories'))