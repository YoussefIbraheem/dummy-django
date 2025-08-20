from app.factories import AuthorFactory
from django.core.management.base import BaseCommand
from app.models import Author
from django.contrib.auth.models import User
import logging

logger = logging.getLogger(__name__)

class Command(BaseCommand):
    help = 'Seed the database with authors'

    def handle(self, *args, **kwargs):
        author_factory = AuthorFactory()
        for _ in range(10):  # Create 10 authors
            author_data = author_factory.create()
            user = User.objects.create_user(
                username=author_data['email'],
                email=author_data['email'],
                first_name=author_data['name'].split()[0],
                last_name=' '.join(author_data['name'].split()[1:]),
                password='password123'
            )
            Author.objects.create(
                user=user,
                bio=author_data['bio']
            )
        self.stdout.write(self.style.SUCCESS('Successfully seeded authors'))
        logger.info("Successfully seeded authors") 

