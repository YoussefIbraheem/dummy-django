from django.db.models.signals import pre_save
from django.dispatch import receiver
from slugify import slugify
from app.models import Category, Tag, Author, Article

@receiver(pre_save, sender=Category)
def set_category_slug(sender, instance, **kwargs):
    if not instance.slug:
        base_slug = slugify(instance.name)
        instance.slug = base_slug
    

@receiver(pre_save, sender=Tag)
def set_tag_slug(sender, instance, **kwargs):
    if not instance.slug:
        base_slug = slugify(instance.name)
        instance.slug = base_slug


@receiver(pre_save, sender=Article)
def set_article_slug(sender, instance, **kwargs):
    if not instance.slug:
        base_slug = slugify(instance.title)
        slug = base_slug
        counter = 1
        while Article.objects.filter(slug=instance.slug).exists():
            slug = f"{base_slug}-{counter}"
            counter += 1
        instance.slug = slug

        
        