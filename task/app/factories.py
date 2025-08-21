from faker import Faker
from app.models import Category, Tag , Author
from django.contrib.auth.models import User
from slugify import slugify


def get_unique_name(model):
    faker = Faker()

    name = faker.word()
    base_slug = slugify(name)
    while model.objects.filter(slug=base_slug).exists():
        name = Faker.word()
        base_slug = slugify(name)
    return name


class CategoryFactory:
    def __init__(self):
        self.faker = Faker()

    def create(self, **kwargs):

        return {
            "name": kwargs.get("name", get_unique_name(Category)),
            "description": kwargs.get("description", self.faker.sentence()),
        }


class TagFactory:
    def __init__(self):
        self.faker = Faker()

    def create(self, **kwargs):
        return {
            "name": kwargs.get("name", get_unique_name(Tag)),
            "color": kwargs.get("color", self.faker.hex_color()),
        }



class AuthorFactory:
    def __init__(self):
        self.faker = Faker()

    def create(self, **kwargs):
        return {
            "name": kwargs.get("name", self.faker.name()),
            "email": kwargs.get("email", self.faker.email()),
            "bio": kwargs.get("bio", self.faker.text(max_nb_chars=200)),
        }
        

class ArticleFactory:
    def __init__(self):
        self.faker = Faker()

    def create(self, **kwargs):
        return {
            "title": kwargs.get("title", self.faker.sentence()),
            "content": kwargs.get("content", self.faker.text(max_nb_chars=500)),
            "slug": kwargs.get("slug", slugify(kwargs.get("title", self.faker.sentence()))),
            "author": kwargs.get("author", Author.objects.first()),
            "category": kwargs.get("category", Category.objects.first()),
        }