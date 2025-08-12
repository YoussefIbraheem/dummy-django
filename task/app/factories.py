from faker import Faker
from app.models import Category, Tag
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
            'name': kwargs.get('name', get_unique_name(Category)),
            'description': kwargs.get('description', self.faker.sentence())
        }

class TagFactory:
    def __init__(self):
        self.faker = Faker()
        


    def create(self, **kwargs):
        return {
            'name': kwargs.get('name', get_unique_name(Tag)),
            'color': kwargs.get('color', self.faker.hex_color())
        }
        
