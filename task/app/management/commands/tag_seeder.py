from django.core.management.base import BaseCommand, CommandError
from app.factories import TagFactory
from app.models import Tag


class Command(BaseCommand):
    help = 'Seed tags into the database'

    def handle(self, *args, **kwargs):
        factory = TagFactory()
        for _ in range(20):
            try:# Adjust the number of tags to create
                tag_data = factory.create()
                Tag.objects.get_or_create(**tag_data)
            except Exception as e:
                raise CommandError(f'Error seeding tags: {e}')
        self.stdout.write(self.style.SUCCESS('Successfully seeded tags'))